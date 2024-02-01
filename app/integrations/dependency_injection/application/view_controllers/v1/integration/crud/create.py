from dependency_injector import containers, providers

from app.integrations.application.view_controllers.v1.integration.v1.common.input_mapping_service import (
    IntegrationCrudInputMappingServiceV1,
)
from app.integrations.application.view_controllers.v1.integration.v1.crud.create import (
    CreateIntegrationViewControllerV1,
)
from app.integrations.dependency_injection.infrastructure.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)


class CreateIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateIntegrationViewControllerV1,
        input_mapping_service=IntegrationCrudInputMappingServiceV1(),
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
