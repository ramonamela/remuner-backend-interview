from app.users.api.v1.user.v2.common.view_models import UserInputV2
from app.users.domain.bo.user_bo import UserBO


class UserInputMappingServiceV2:

    def __call__(self, input_user: UserInputV2) -> UserBO:
        return UserBO(
            first_name=input_user.name,
            last_name=input_user.last_name,
            email=input_user.email,
            team_ids=input_user.teams,
        )
