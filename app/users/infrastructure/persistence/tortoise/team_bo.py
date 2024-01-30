from tortoise.exceptions import IntegrityError

from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.persistence.exceptions import RepeatedTeamNameException
from app.users.models import Team


class TeamBOTortoisePersistenceService(TeamBOPersistenceInterface):

    async def create(self, team_bo: TeamBO):
        try:
            new_team = await Team.create(name=team_bo.name)
        except IntegrityError as exc:
            if 'duplicate key value violates unique constraint "teams_name_key"' in str(exc):
                raise RepeatedTeamNameException()
            raise exc
        team_bo.id = new_team.team_id
        return new_team.team_id
