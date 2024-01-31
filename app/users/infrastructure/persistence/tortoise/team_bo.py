import asyncio

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.persistence.exceptions.team_bo import RepeatedTeamNameException
from app.users.infrastructure.persistence.exceptions.user_bo import UserNotFoundException
from app.users.models import Team, User


class TeamBOTortoisePersistenceService(TeamBOPersistenceInterface):

    @classmethod
    async def _add_to_team(cls, team, user_ids):
        users = await User.filter(user_id__in=user_ids).only("user_id")
        if len(users) != len(user_ids):
            raise UserNotFoundException()
        tasks = [team.users.add(user) for user in users]
        await asyncio.gather(*tasks)

    @transactions.atomic()
    async def create(self, team_bo: TeamBO):
        try:
            new_team = await Team.create(name=team_bo.name)
        except IntegrityError as exc:
            if 'duplicate key value violates unique constraint "teams_name_key"' in str(exc):
                raise RepeatedTeamNameException()
            raise exc
        if team_bo.user_ids is not None and len(team_bo.user_ids) > 0:
            await self._add_to_team(new_team, team_bo.user_ids)
        team_bo.id = new_team.team_id
        return new_team.team_id
