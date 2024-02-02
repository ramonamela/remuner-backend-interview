from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.integrations.enums import IntegrationStatus


class CreateIntegrationViewControllerV1:
    def __init__(self, integration_bo_persistence_service):
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, integration_bo: IntegrationBO):
        integration_bo.status = IntegrationStatus.ACTIVE
        return await self.integration_bo_persistence_service.create(integration_bo=integration_bo)
