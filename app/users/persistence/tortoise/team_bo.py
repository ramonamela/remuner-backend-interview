import asyncio
from typing import List

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.exceptions.team_bo import (
    RepeatedTeamNameException,
    TeamNotFoundException,
)
from app.users.domain.persistence.exceptions.user_bo import UserNotFoundException
from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)
from app.users.models import Team, User
from app.users.persistence.tortoise.services.team_bo_mapping_service import (
    TeamBOMappingService,
)
from app.users.persistence.tortoise.services.user_bo_mapping_service import (
    UserBOMappingService,
)


class TeamBOTortoisePersistenceService(TeamBOPersistenceInterface):

    def __init__(self):
        self.user_bo_mapping_service = UserBOMappingService()
        self.team_bo_mapping_service = TeamBOMappingService()

    @classmethod
    async def _add_users_to_team(cls, team, user_ids):
        users = await User.filter(user_id__in=user_ids).only("user_id")
        if len(users) != len(user_ids):
            raise UserNotFoundException()
        remove_tasks = []
        if len(team.users) > 0:
            remove_tasks = [
                team.users.remove(user) for user in team.users if user.user_id not in user_ids
            ]
        add_tasks = [team.users.add(user) for user in users if user.user_id in user_ids]
        await asyncio.gather(*add_tasks, *remove_tasks)

    @transactions.atomic()
    async def create(self, team_bo: TeamBO) -> int:
        try:
            new_team = await Team.create(name=team_bo.name)
            await new_team.fetch_related("users")
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedTeamNameException()
            raise exc
        if team_bo.user_ids is not None and len(team_bo.user_ids) > 0:
            await self._add_users_to_team(new_team, team_bo.user_ids)
        team_bo.id = new_team.team_id
        return new_team.team_id

    @transactions.atomic()
    async def update(self, team_bo: TeamBO) -> id:
        try:
            team_to_update = await Team.get(team_id=team_bo.id).prefetch_related(
                "users",
            )
        except Exception:
            raise TeamNotFoundException()
        try:
            await team_to_update.update_from_dict(
                {
                    "name": team_bo.name,
                }
            ).save()
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedTeamNameException()
        await self._add_users_to_team(team_to_update, team_bo.user_ids)
        # await self._add_integrations_to_user(user_to_update, user_bo.team_ids)
        return team_to_update.team_id

    def _generate_bo(self, team: Team) -> TeamBO:
        team_bo = self.team_bo_mapping_service(team=team)
        team_bo.users = list(map(lambda user: self.user_bo_mapping_service(user), team.users))
        return team_bo

    async def get_all(self) -> List[TeamBO]:
        teams = await Team.filter().prefetch_related("users")
        return list(map(lambda team: self._generate_bo(team), teams))

    async def get(self, team_id: int) -> TeamBO:
        team = await Team.get(team_id=team_id).prefetch_related("users")
        return self._generate_bo(team=team)

    async def delete(self, team_id: int):
        object_to_delete = await Team.get(team_id=team_id)
        if object_to_delete:
            await object_to_delete.delete()
        else:
            raise TeamNotFoundException()

    async def count_elements(self):
        return await Team.filter().count()
