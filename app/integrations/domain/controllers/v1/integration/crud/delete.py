from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)


class DeleteIntegrationControllerV1:
    def __init__(self, integration_bo_persistence_service):
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, integration_id: int):
        await self.integration_bo_persistence_service.delete(integration_id=integration_id)
