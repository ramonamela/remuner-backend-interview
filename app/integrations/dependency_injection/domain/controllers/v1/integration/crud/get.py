from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.crud.get import (
    GetIntegrationControllerV1,
)


class GetIntegrationControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetIntegrationControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
