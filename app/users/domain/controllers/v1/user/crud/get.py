from typing import List, Optional, Union

from app.users.api.v1.user.v1.common import (
    UserCrudOutputMappingServiceV1,
)
from app.users.api.v1.user.v1.crud.view_models import (
    UserCrudOutputV1,
)
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class GetUserViewControllerV1:
    def __init__(self, output_mapping_service, user_bo_persistence_service):
        self.output_mapping_service: UserCrudOutputMappingServiceV1 = output_mapping_service
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(
        self, user_id: Optional[int] = None
    ) -> Union[UserCrudOutputV1, List[UserCrudOutputV1]]:
        if user_id is None:
            user_bos = await self.user_bo_persistence_service.get_all()
            return [self.output_mapping_service(user_bo=user_bo) for user_bo in user_bos]
        else:
            user_bo = await self.user_bo_persistence_service.get(user_id=user_id)
            return self.output_mapping_service(user_bo=user_bo)
