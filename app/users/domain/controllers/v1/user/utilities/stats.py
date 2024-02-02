from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class GetUsersStatsControllerV1:
    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self):
        return await self.user_bo_persistence_service.count_elements()
