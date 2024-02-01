import asyncio
from typing import List

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.integrations.infrastructure.persistence.tortoise.services.integration_bo_mapping_service import (
    IntegrationBOMappingService,
)
from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.infrastructure.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.infrastructure.persistence.exceptions.user_bo import (
    RepeatedEmailException,
    UserHasIntegrationsException,
    UserNotFoundException,
)
from app.users.infrastructure.persistence.tortoise.services.team_bo_mapping_service import (
    TeamBOMappingService,
)
from app.users.infrastructure.persistence.tortoise.services.user_bo_mapping_service import (
    UserBOMappingService,
)
from app.users.models import Team, User


class UserBOTortoisePersistenceService(UserBOPersistenceInterface):

    def __init__(self):
        self.user_bo_mapping_service = UserBOMappingService()
        self.team_bo_mapping_service = TeamBOMappingService()
        self.integration_bo_mapping_service = IntegrationBOMappingService()

    @classmethod
    async def _add_to_user(cls, user, team_ids):
        teams = await Team.filter(team_id__in=team_ids).only("team_id")
        if len(teams) != len(team_ids):
            raise TeamNotFoundException()
        tasks = [user.teams.add(team) for team in teams]
        await asyncio.gather(*tasks)

    @transactions.atomic()
    async def create(self, user_bo: UserBO):
        try:
            new_user = await User.create(
                first_name=user_bo.first_name,
                last_name=user_bo.last_name,
                email=user_bo.email,
                status=user_bo.status,
            )
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedEmailException()
            raise exc
        if user_bo.team_ids is not None and len(user_bo.team_ids) > 0:
            await self._add_to_user(new_user, user_bo.team_ids)
        user_bo.id = new_user.user_id
        return new_user.user_id

    def _generate_bo(self, user: User) -> UserBO:
        user_bo = self.user_bo_mapping_service(user=user)
        user_bo.teams = list(map(lambda team: self.team_bo_mapping_service(team), user.teams))
        user_bo.integrations = list(
            map(
                lambda integration: self.integration_bo_mapping_service(integration),
                user.integrations,
            )
        )
        return user_bo

    async def get_all(self) -> List[UserBO]:
        users = await User.filter().prefetch_related("teams", "integrations")
        return list(map(lambda user: self._generate_bo(user), users))

    async def get(self, user_id: int) -> UserBO:
        user = await User.get(user_id=user_id).prefetch_related("teams", "integrations")
        return self._generate_bo(user=user)

    async def delete(self, user_id: int):
        object_to_delete = await User.get(user_id=user_id).prefetch_related("integrations")
        if object_to_delete:
            if len(object_to_delete.integrations) > 0:
                raise UserHasIntegrationsException()
            await object_to_delete.delete()
        else:
            raise UserNotFoundException()
