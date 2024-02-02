from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.crud.get import (
    GetIntegrationViewControllerV1,
)


class GetIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetIntegrationViewControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
