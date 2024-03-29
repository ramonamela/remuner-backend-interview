from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.utilities.stats import (
    GetIntegrationsStatsControllerV1,
)


class GetIntegrationsStatsControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetIntegrationsStatsControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
