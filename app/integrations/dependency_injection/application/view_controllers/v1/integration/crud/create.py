from app.integrations.dependency_injection.application.view_controllers.v1.integration.common.input_mapping_service import (
    IntegrationCrudInputMappingServiceV1,
)
from app.integrations.domain.persistence.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudIdOutputV1,
    IntegrationCrudInputV1,
)


class CreateIntegrationViewControllerV1:
    def __init__(self, input_mapping_service, integration_bo_persistence_service):
        self.input_mapping_service: IntegrationCrudInputMappingServiceV1 = input_mapping_service
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, input_team: IntegrationCrudInputV1):
        integration_bo = self.input_mapping_service(input_team)
        await self.integration_bo_persistence_service.create(integration_bo=integration_bo)
        return IntegrationCrudIdOutputV1(id=integration_bo.id)
