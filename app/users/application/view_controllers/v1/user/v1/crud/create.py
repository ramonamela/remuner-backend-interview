from app.users.application.view_controllers.v1.user.v1.common.input_mapping_service import (
    UserCrudInputMappingServiceV1,
)
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudInputV1,
    UserCrudIdOutputV1,
)


class CreateUserViewControllerV1:
    def __init__(self, input_mapping_service, user_bo_persistence_service):
        self.input_mapping_service: UserCrudInputMappingServiceV1 = input_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, input_user: UserCrudInputV1):
        user_bo = self.input_mapping_service(input_user)
        user_bo.status = UserStatus.ACTIVE
        await self.user_bo_persistence_service.create(user_bo=user_bo)
        return UserCrudIdOutputV1(id=user_bo.id)
