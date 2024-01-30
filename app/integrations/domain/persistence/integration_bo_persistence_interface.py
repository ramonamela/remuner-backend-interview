from abc import ABC, abstractmethod

from app.integrations.domain.bo.integration_bo import IntegrationBO


class IntegrationBOPersistenceInterface(ABC):
    @abstractmethod
    def create(self, integration_bo: IntegrationBO):
        pass
