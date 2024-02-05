from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.users.domain.persistence.exceptions.user_bo import UserHasIntegrationsException
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class DeleteUserControllerV1:
    def __init__(self, user_bo_persistence_service, integration_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service
        self.integration_bo_persistence_services: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, user_id: int):
        integration_bos = await self.integration_bo_persistence_services.get_integrations_for_user(
            user_id=user_id
        )
        if len(integration_bos) > 0:
            raise UserHasIntegrationsException()
        await self.user_bo_persistence_service.delete(user_id=user_id)
