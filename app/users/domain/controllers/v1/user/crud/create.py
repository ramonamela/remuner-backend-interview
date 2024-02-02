from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)
from app.users.enums import UserStatus


class CreateUserControllerV1:
    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_bo: UserBO):
        user_bo.status = UserStatus.ACTIVE
        return await self.user_bo_persistence_service.create(user_bo=user_bo)
