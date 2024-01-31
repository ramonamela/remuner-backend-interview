from typing import List, Optional, Union

from app.users.application.view_controllers.v1.user.v2.common.output_mapping_service import (
    UserCrudOutputMappingServiceV2,
)
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.infrastructure.api.v1.user.v2.crud.view_models import UserCrudOutputV2


class GetUserViewControllerV2:
    def __init__(self, output_mapping_service, user_bo_persistence_service):
        self.output_mapping_service: UserCrudOutputMappingServiceV2 = output_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(
        self, user_id: Optional[int] = None
    ) -> Union[UserCrudOutputV2, List[UserCrudOutputV2]]:
        if user_id is None:
            user_bos = await self.user_bo_persistence_service.get_all()
            return [self.output_mapping_service(user_bo=user_bo) for user_bo in user_bos]
        else:
            user_bo = await self.user_bo_persistence_service.get(user_id=user_id)
            return self.output_mapping_service(user_bo=user_bo)
