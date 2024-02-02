from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class DeleteUserViewControllerV1:
    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, user_id: int):
        await self.user_bo_persistence_service.delete(user_id=user_id)
