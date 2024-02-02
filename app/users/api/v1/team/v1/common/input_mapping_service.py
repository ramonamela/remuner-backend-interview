from app.users.api.v1.team.v1.common.view_models import TeamInputV1
from app.users.domain.bo.team_bo import TeamBO


class TeamInputMappingServiceV1:

    def __call__(self, input_team: TeamInputV1) -> TeamBO:
        input_team_dict = input_team.model_dump()
        return TeamBO(user_ids=input_team_dict.pop("users"), **input_team_dict)
