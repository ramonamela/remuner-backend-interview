from app.users.domain.bo.user_bo import UserBO
from app.users.infrastructure.api.v1.user.v1.crud.view_models import UserCrudPostInputV1


class UserCrudPostInputMappingServiceV1:

    def __call__(self, input_team: UserCrudPostInputV1):
        return UserBO(**input_team.model_dump())
