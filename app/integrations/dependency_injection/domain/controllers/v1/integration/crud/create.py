from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.controllers.v1.integration.crud.create import (
    CreateIntegrationControllerV1,
)


class CreateIntegrationControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateIntegrationControllerV1,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
