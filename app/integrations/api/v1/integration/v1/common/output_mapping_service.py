from app.integrations.api.v1.integration.v1.common.view_models import IntegrationOutputV1
from app.integrations.domain.bo.integration_bo import IntegrationBO


class IntegrationOutputMappingServiceV1:

    async def __call__(self, integration_bo: IntegrationBO) -> IntegrationOutputV1:
        return IntegrationOutputV1(
            id=integration_bo.id,
            name=integration_bo.name,
            user_first_name=integration_bo.user.first_name,
            user_last_name=integration_bo.user.last_name,
            user_email=integration_bo.user.email,
            status=integration_bo.status,
        )
