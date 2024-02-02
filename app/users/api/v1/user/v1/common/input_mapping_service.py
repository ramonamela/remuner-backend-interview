from app.users.api.v1.user.v1.common.view_models import UserInputV1
from app.users.domain.bo.user_bo import UserBO


class UserInputMappingServiceV1:

    def __call__(self, input_user: UserInputV1) -> UserBO:
        input_user_dict = input_user.model_dump()
        return UserBO(team_ids=input_user_dict.pop("teams"), **input_user_dict)
