from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)


class CountIntegrationControllerV1:
    def __init__(self, integration_bo_persistence_service):
        self.integration_bo_persistence_service: TeamBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self):
        return await self.integration_bo_persistence_service.count()
