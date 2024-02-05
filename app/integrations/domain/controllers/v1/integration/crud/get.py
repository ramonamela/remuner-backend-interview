from typing import List, Optional, Union

from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class GetIntegrationControllerV1:
    def __init__(self, integration_bo_persistence_service, user_bo_persistence_service):
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service

    async def __call__(
        self, integration_id: Optional[int] = None
    ) -> Union[IntegrationBO, List[IntegrationBO]]:
        if integration_id is None:
            integration_bos = await self.integration_bo_persistence_service.get_all()
            user_bo_ids = set(map(lambda integration_bo: integration_bo.user_id, integration_bos))
            user_bos_dict = {
                user_bo.id: user_bo
                for user_bo in await self.user_bo_persistence_service.get_users_in(
                    user_ids=user_bo_ids
                )
            }
            for integration_bo in integration_bos:
                integration_bo.user = user_bos_dict[integration_bo.user_id]
            return integration_bos
        else:
            integration_bo = await self.integration_bo_persistence_service.get(
                integration_id=integration_id
            )
            integration_bo.user = await self.user_bo_persistence_service.get(
                user_id=integration_bo.user_id
            )
            return integration_bo
