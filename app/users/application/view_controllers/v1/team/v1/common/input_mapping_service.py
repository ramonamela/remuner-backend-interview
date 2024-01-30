from app.users.domain.bo.team_bo import TeamBO
from app.users.infrastructure.api.v1.team.v1.crud.view_models import TeamCrudPostInputV1


class TeamCrudPostInputMappingServiceV1:

    def __call__(self, input_team: TeamCrudPostInputV1):
        return TeamBO(**input_team.model_dump())
