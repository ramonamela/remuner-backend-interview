import asyncio
from typing import List

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.domain.persistence.exceptions.user_bo import (
    RepeatedEmailException,
    UserHasIntegrationsException,
    UserNotFoundException,
)
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)
from app.users.models import Team, User
from app.users.persistence.tortoise.services.team_bo_mapping_service import (
    TeamBOMappingService,
)
from app.users.persistence.tortoise.services.user_bo_mapping_service import (
    UserBOMappingService,
)


class UserBOTortoisePersistenceService(UserBOPersistenceInterface):

    def __init__(self):
        self.user_bo_mapping_service = UserBOMappingService()
        self.team_bo_mapping_service = TeamBOMappingService()

    @classmethod
    async def _add_teams_to_user(cls, user, team_ids):
        teams = await Team.filter(team_id__in=team_ids).only("team_id")
        if len(teams) != len(team_ids):
            raise TeamNotFoundException()
        remove_users = []
        if len(user.teams) > 0:
            remove_users = [
                user.teams.remove(team) for team in user.teams if team.team_id not in team_ids
            ]
        add_users = [user.teams.add(team) for team in teams if team.team_id in team_ids]
        await asyncio.gather(*add_users, *remove_users)

    @transactions.atomic()
    async def create(self, user_bo: UserBO) -> int:
        try:
            new_user = await User.create(
                first_name=user_bo.first_name,
                last_name=user_bo.last_name,
                email=user_bo.email,
                status=user_bo.status,
            )
            await new_user.fetch_related("teams")
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedEmailException()
            raise exc
        if user_bo.team_ids is not None and len(user_bo.team_ids) > 0:
            await self._add_teams_to_user(new_user, user_bo.team_ids)
        user_bo.id = new_user.user_id
        return new_user.user_id

    @transactions.atomic()
    async def update(self, user_bo: UserBO) -> int:
        try:
            user_to_update = await User.get(user_id=user_bo.id).prefetch_related(
                "teams", "integrations"
            )
        except Exception:
            raise UserNotFoundException()
        try:
            await user_to_update.update_from_dict(
                {
                    "first_name": user_bo.first_name,
                    "last_name": user_bo.last_name,
                    "email": user_bo.email,
                    "status": user_bo.status,
                }
            ).save()
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedEmailException()
        await self._add_teams_to_user(user_to_update, user_bo.team_ids)
        return user_to_update.user_id

    def _generate_bo(self, user: User) -> UserBO:
        user_bo = self.user_bo_mapping_service(user=user)
        user_bo.teams = []
        user_bo.team_ids = []
        for team in user.teams:
            user_bo.teams.append(self.team_bo_mapping_service(team))
            user_bo.team_ids.append(user_bo.teams[-1].id)
        return user_bo

    async def get_all(self) -> List[UserBO]:
        return [self._generate_bo(user) for user in await User.filter().prefetch_related("teams")]

    async def get_users_in(self, user_ids: List[int]):
        return [
            self._generate_bo(user)
            for user in await User.filter(user_id__in=user_ids).prefetch_related("teams")
        ]

    async def get(self, user_id: int) -> UserBO:
        return self._generate_bo(await User.get(user_id=user_id).prefetch_related("teams"))

    async def delete(self, user_id: int):
        object_to_delete = await User.get(user_id=user_id)
        if object_to_delete:
            await object_to_delete.delete()
        else:
            raise UserNotFoundException()

    async def count_elements(self):
        return await User.filter().count()
