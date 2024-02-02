from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.crud.update import (
    UpdateIntegrationViewControllerV1,
)


class UpdateIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        UpdateIntegrationViewControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
