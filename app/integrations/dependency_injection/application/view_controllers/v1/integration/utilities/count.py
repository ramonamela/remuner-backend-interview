from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.utilities.count import (
    CountIntegrationViewControllerV1,
)


class CountIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CountIntegrationViewControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
