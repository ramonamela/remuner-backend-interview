from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class UpdateUserControllerV1:
    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_id: int, user_bo: UserBO):
        user_bo.id = user_id
        return await self.user_bo_persistence_service.update(user_bo=user_bo)
