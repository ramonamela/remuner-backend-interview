from app.users.application.view_controllers.v1.user.v1.common.input_mapping_service import (
    UserCrudInputMappingServiceV1,
)
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudInputV1,
    UserCrudIdOutputV1,
)


class GetUserViewControllerV1:
    def __init__(self, output_mapping_service, user_bo_persistence_service):
        self.output_mapping_service: UserCrudGetOutputMappingServiceV1 = output_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_id):
        await self.user_bo_persistence_service.get(user_id=user_id)
        return UserCrudIdOutputV1(id=user_bo.id)
