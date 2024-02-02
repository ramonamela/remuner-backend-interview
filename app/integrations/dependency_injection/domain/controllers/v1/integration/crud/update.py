from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.crud.update import (
    UpdateIntegrationControllerV1,
)


class UpdateIntegrationControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        UpdateIntegrationControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
