from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.models import Integration


class IntegrationBOMappingService:
    def __call__(self, integration: Integration) -> IntegrationBO:
        return IntegrationBO(
            id=integration.integration_id,
            name=integration.name,
            token=integration.token,
            status=integration.status,
        )
