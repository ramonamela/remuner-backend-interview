from typing import List, Optional, Union

from app.integrations.domain.persistence.interfaces.integration_bo_persistence_interface import (
    IntegrationBOPersistenceInterface,
)
from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.interfaces.user_bo_persistence_interface import (
    UserBOPersistenceInterface,
)


class GetUserControllerV1:
    def __init__(self, user_bo_persistence_service, integration_bo_persistence_service):
        self.user_bo_persistence_service: UserBOPersistenceInterface = user_bo_persistence_service
        self.integration_bo_persistence_service: IntegrationBOPersistenceInterface = (
            integration_bo_persistence_service
        )

    async def __call__(self, user_id: Optional[int] = None) -> Union[UserBO, List[UserBO]]:
        if user_id is None:
            # Note that even if several iterations are done, only two database queries are performed (No N + 1 queries)
            user_bos = await self.user_bo_persistence_service.get_all()
            user_bos_dict = {}
            for user_bo in user_bos:
                user_bo.integrations = []
                user_bos_dict[user_bo.id] = user_bo
            user_ids = set(map(lambda user_bo: user_bo.id, user_bos))
            integration_bos = (
                await self.integration_bo_persistence_service.get_integrations_for_users_in(
                    user_ids=user_ids
                )
            )
            for integration_bo in integration_bos:
                user_bos_dict[integration_bo.user_id] = integration_bo
            return user_bos
        else:
            user_bo = await self.user_bo_persistence_service.get(user_id=user_id)
            user_bo.integrations = (
                await self.integration_bo_persistence_service.get_integrations_for_user(
                    user_id=user_bo.id
                )
            )
            return user_bo
