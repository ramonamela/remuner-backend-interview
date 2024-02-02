from typing import List, Optional, Union

from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class GetUserControllerV1:
    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_id: Optional[int] = None) -> Union[UserBO, List[UserBO]]:
        if user_id is None:
            return await self.user_bo_persistence_service.get_all()
        else:
            return await self.user_bo_persistence_service.get(user_id=user_id)
