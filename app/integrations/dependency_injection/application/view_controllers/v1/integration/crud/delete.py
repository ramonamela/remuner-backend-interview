from dependency_injector import containers, providers

from app.integrations.application.view_controllers.v1.integration.v1.crud.delete import (
    DeleteIntegrationViewControllerV1,
)
from app.integrations.dependency_injection.infrastructure.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)


class DeleteIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteIntegrationViewControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
