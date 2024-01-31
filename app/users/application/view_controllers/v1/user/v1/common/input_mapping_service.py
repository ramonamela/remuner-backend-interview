from app.users.domain.bo.user_bo import UserBO
from app.users.infrastructure.api.v1.user.v1.crud.view_models import UserCrudPostInputV1


class UserCrudPostInputMappingServiceV1:

    def __call__(self, input_user: UserCrudPostInputV1):
        input_user_dict = input_user.model_dump()
        return UserBO(team_ids=input_user_dict.pop("teams"), **input_user_dict)
