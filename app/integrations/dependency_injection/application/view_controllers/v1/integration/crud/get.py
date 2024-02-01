from dependency_injector import containers, providers

from app.integrations.application.view_controllers.v1.integration.v1.common.output_mapping_service import (
    IntegrationCrudOutputMappingServiceV1,
)
from app.integrations.application.view_controllers.v1.integration.v1.crud.get import (
    GetIntegrationViewControllerV1,
)
from app.integrations.dependency_injection.infrastructure.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)


class GetIntegrationViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetIntegrationViewControllerV1,
        output_mapping_service=IntegrationCrudOutputMappingServiceV1(),
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
