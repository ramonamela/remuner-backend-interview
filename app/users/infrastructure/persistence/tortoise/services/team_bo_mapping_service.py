from app.users.domain.bo.team_bo import TeamBO
from app.users.models import Team


class TeamBOMappingService:
    def __call__(self, team: Team) -> TeamBO:
        return TeamBO(id=team.team_id, name=team.name)
