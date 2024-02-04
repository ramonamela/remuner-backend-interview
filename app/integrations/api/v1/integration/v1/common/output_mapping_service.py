from app.integrations.api.v1.integration.v1.common.view_models import IntegrationOutputV1
from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import UserBOPersistenceInterface


class IntegrationOutputMappingServiceV1:

    def __init__(self, user_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(self, integration_bo: IntegrationBO) -> IntegrationOutputV1:
        integration_bo.user = await self.user_bo_persistence_service.get(user_id=integration_bo.user_id)
        return IntegrationOutputV1(
            id=integration_bo.id,
            name=integration_bo.name,
            user_first_name=integration_bo.user.first_name,
            user_last_name=integration_bo.user.last_name,
            user_email=integration_bo.user.email,
            status=integration_bo.status,
        )
