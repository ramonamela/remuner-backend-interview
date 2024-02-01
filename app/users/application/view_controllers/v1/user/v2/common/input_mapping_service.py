from app.users.domain.bo.user_bo import UserBO
from app.users.infrastructure.api.v1.user.v2.crud.view_models import UserCrudInputV2


class UserCrudInputMappingServiceV2:

    def __call__(self, input_user: UserCrudInputV2) -> UserBO:
        return UserBO(
            first_name=input_user.name,
            last_name=input_user.last_name,
            email=input_user.email,
            team_ids=input_user.teams,
        )
