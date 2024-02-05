from abc import ABC, abstractmethod
from typing import List

from app.integrations.domain.bo.integration_bo import IntegrationBO


class IntegrationBOPersistenceInterface(ABC):
    @abstractmethod
    async def create(self, integration_bo: IntegrationBO):
        pass

    @abstractmethod
    async def update(self, integration_bo: IntegrationBO):
        pass

    @abstractmethod
    async def get_all(self) -> List[IntegrationBO]:
        pass

    @abstractmethod
    async def get(self, integration_id: int) -> IntegrationBO:
        pass

    @abstractmethod
    async def get_integrations_for_user(self, user_id: int):
        pass

    @abstractmethod
    async def count_integrations_for_user(self, user_id: int):
        pass

    @abstractmethod
    async def get_integrations_for_users_in(self, user_ids: List[int]):
        pass

    @abstractmethod
    async def delete(self, integration_id: int):
        pass

    @abstractmethod
    async def count_elements(self):
        pass
