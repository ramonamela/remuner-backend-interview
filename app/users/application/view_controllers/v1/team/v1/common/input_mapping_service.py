from app.users.domain.bo.team_bo import TeamBO
from app.users.infrastructure.api.v1.team.v1.crud.view_models import TeamCrudInputV1


class TeamCrudInputMappingServiceV1:

    def __call__(self, input_team: TeamCrudInputV1) -> TeamBO:
        input_team_dict = input_team.model_dump()
        return TeamBO(user_ids=input_team_dict.pop("users"), **input_team_dict)
