from app.users.application.view_controllers.v1.user.v2.common.input_mapping_service import (
    UserCrudInputMappingServiceV2,
)
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.infrastructure.api.v1.user.v2.crud.view_models import (
    UserCrudIdOutputV2,
    UserCrudInputV2,
)


class UpdateUserViewControllerV2:
    def __init__(self, input_mapping_service, user_bo_persistence_service):
        self.input_mapping_service: UserCrudInputMappingServiceV2 = input_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_id: int, input_user: UserCrudInputV2):
        input_user.id = user_id
        user_bo = self.input_mapping_service(input_user)
        await self.user_bo_persistence_service.update(user_bo=user_bo)
        return UserCrudIdOutputV2(id=user_bo.id)
