from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.utilities.count import (
    CountIntegrationControllerV1,
)


class CountIntegrationControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CountIntegrationControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
