from typing import List

from tortoise import transactions

from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.infrastructure.persistence.exceptions.integration_bo import (
    IntegrationNotFoundException,
)
from app.integrations.infrastructure.persistence.tortoise.services.integration_bo_mapping_service import (
    IntegrationBOMappingService,
)
from app.integrations.models import Integration
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.persistence.tortoise.services.user_bo_mapping_service import (
    UserBOMappingService,
)
from app.users.models import Team


class IntegrationBOTortoisePersistenceService(TeamBOPersistenceInterface):

    def __init__(self):
        self.integration_bo_mapping_service = IntegrationBOMappingService()
        self.user_bo_mapping_service = UserBOMappingService()

    @transactions.atomic()
    async def create(self, integration_bo: IntegrationBO):
        # Add exception in case integration_bo.user.user_id and integration_bo.user_id are both None
        new_integration = await Integration.create(
            name=integration_bo.name,
            token=integration_bo.token,
            user_id=(
                integration_bo.user_id if integration_bo.user_id else integration_bo.user.user_id
            ),
            status=integration_bo.status,
        )
        integration_bo.id = new_integration.integration_id
        return new_integration.integration_id

    def _generate_bo(self, integration: Integration) -> IntegrationBO:
        integration_bo = self.integration_bo_mapping_service(integration=integration)
        integration_bo.user = self.user_bo_mapping_service(integration.user)
        return integration_bo

    async def get_all(self) -> List[IntegrationBO]:
        integrations = await Integration.filter().prefetch_related("user")
        return list(map(lambda integration: self._generate_bo(integration), integrations))

    async def get(self, integration_id: int) -> IntegrationBO:
        integration = await Team.get(integration_id=integration_id).prefetch_related("users")
        return self._generate_bo(integration=integration)

    async def delete(self, integration_id: int):
        object_to_delete = await Integration.get(integration_id=integration_id)
        if object_to_delete:
            await object_to_delete.delete()
        else:
            raise IntegrationNotFoundException()
