from typing import List

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.config import key_value_settings
from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.domain.persistence.exceptions.integration_bo import (
    IntegrationNotFoundException,
    RepeatedIntegrationNameException,
)
from app.integrations.models import Integration
from app.integrations.persistence.tortoise.services.integration_bo_mapping_service import (
    IntegrationBOMappingService,
)
from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)
from app.users.models import Team
from app.users.persistence.tortoise.services.user_bo_mapping_service import (
    UserBOMappingService,
)
from remuner_library.persistences.key_value_store.key_value_interface import KeyValueInterface
import asyncio
from typing import Optional
class IntegrationBOCachedTortoisePersistenceService(TeamBOPersistenceInterface):


    def __init__(self, key_value_store: Optional[KeyValueInterface] = None):
        self.integration_bo_mapping_service = IntegrationBOMappingService()
        self.user_bo_mapping_service = UserBOMappingService()

        self.key_value_store = key_value_store

        self.initialized = False

    async def key_value_store_initialization(self):
        if self.key_value_store is not None and not self.initialized:
            counter = await Integration.filter().count()
            await self.key_value_store.set_if_not_exists(key_value_settings.integrations_counter_key, counter)
            self.initialized = True

    @transactions.atomic()
    async def create(self, integration_bo: IntegrationBO):
        if self.key_value_store is not None and not self.initialized:
            await self.key_value_store_initialization()
        # Add exception in case integration_bo.user.user_id and integration_bo.user_id are both None
        try:
            new_integration = await Integration.create(
                name=integration_bo.name,
                token=integration_bo.token,
                user_id=(
                    integration_bo.user_id
                    if integration_bo.user_id
                    else integration_bo.user.user_id
                ),
                status=integration_bo.status,
            )
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedIntegrationNameException()
            raise exc
        integration_bo.id = new_integration.integration_id
        await self.key_value_store.atomic_key_increment(key_value_settings.integrations_counter_key)
        return new_integration.integration_id

    @transactions.atomic()
    async def update(self, integration_bo: IntegrationBO):
        try:
            integration_to_update = await Integration.get(integration_id=integration_bo.id)
        except Exception:
            raise IntegrationNotFoundException
        try:
            # Only update token if provided
            update_dict = {
                "name": integration_bo.name,
                "user_id": integration_bo.user_id,
            }
            if integration_bo.token is not None:
                update_dict.update(token=integration_bo.token)
            await integration_to_update.update_from_dict(update_dict).save()
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedIntegrationNameException()
        return integration_to_update.integration_id

    def _generate_bo(self, integration: Integration) -> IntegrationBO:
        integration_bo = self.integration_bo_mapping_service(integration=integration)
        integration_bo.user = self.user_bo_mapping_service(integration.user)
        return integration_bo

    async def get_all(self) -> List[IntegrationBO]:
        integrations = await Integration.filter().prefetch_related("user")
        return list(map(lambda integration: self._generate_bo(integration), integrations))

    async def get(self, integration_id: int) -> IntegrationBO:
        integration = await Integration.get(integration_id=integration_id).prefetch_related("users")
        return self._generate_bo(integration=integration)

    @transactions.atomic()
    async def delete(self, integration_id: int):
        object_to_delete = await Integration.get(integration_id=integration_id)
        if object_to_delete:
            if self.key_value_store is not None and not self.initialized:
                await self.key_value_store_initialization()
            # We could move the transaction atomic here if we allow the counter to differ
            await object_to_delete.delete()
            await self.key_value_store.atomic_key_decrement(key_value_settings.integrations_counter_key)

        else:
            raise IntegrationNotFoundException()

    async def count_elements(self):
        if self.key_value_store is not None and not self.initialized:
            await self.key_value_store_initialization()
        return await self.key_value_store.get(key_value_settings.integrations_counter_key)
