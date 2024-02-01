from typing import List, Optional, Union

from app.integrations.application.view_controllers.v1.integration.v1.common.output_mapping_service import (
    IntegrationCrudOutputMappingServiceV1,
)
from app.integrations.domain.persistence.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudOutputV1,
)


class GetIntegrationViewControllerV1:
    def __init__(self, output_mapping_service, integration_bo_persistence_service):
        self.output_mapping_service: IntegrationCrudOutputMappingServiceV1 = output_mapping_service
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(
        self, integration_id: Optional[int] = None
    ) -> Union[IntegrationCrudOutputV1, List[IntegrationCrudOutputV1]]:
        if integration_id is None:
            integration_bos = await self.integration_bo_persistence_service.get_all()
            return [
                self.output_mapping_service(integration_bo=integration_bo)
                for integration_bo in integration_bos
            ]
        else:
            integration_bo = await self.integration_bo_persistence_service.get(
                integration_id=integration_id
            )
            return self.output_mapping_service(integration_bo=integration_bo)
