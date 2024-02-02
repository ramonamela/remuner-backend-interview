from typing import List, Optional, Union

from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)


class GetIntegrationControllerV1:
    def __init__(self, integration_bo_persistence_service):
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(
        self, integration_id: Optional[int] = None
    ) -> Union[IntegrationBO, List[IntegrationBO]]:
        if integration_id is None:
            return await self.integration_bo_persistence_service.get_all()
        else:
            return await self.integration_bo_persistence_service.get(integration_id=integration_id)
