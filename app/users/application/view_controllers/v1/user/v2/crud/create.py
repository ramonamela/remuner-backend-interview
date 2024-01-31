from app.users.application.view_controllers.v1.user.v2.common.input_mapping_service import (
    UserCrudInputMappingServiceV2,
)
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v2.crud.view_models import (
    UserCrudPostInputV2,
    UserCrudPostOutputV2,
)


class CreateUserViewControllerV2:
    def __init__(self, input_mapping_service, user_bo_persistence_service):
        self.input_mapping_service: UserCrudInputMappingServiceV2 = input_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, input_user: UserCrudPostInputV2):
        user_bo = self.input_mapping_service(input_user)
        user_bo.status = UserStatus.ACTIVE
        await self.user_bo_persistence_service.create(user_bo=user_bo)
        return UserCrudPostOutputV2(id=user_bo.id)
