from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)


class UpdateIntegrationControllerV1:
    def __init__(self, integration_bo_persistence_service):
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, integration_id: int, integration_bo: IntegrationBO) -> int:
        integration_bo.id = integration_id
        return await self.integration_bo_persistence_service.update(integration_bo=integration_bo)
