from app.integrations.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudInputV1,
)
from app.integrations.domain.bo.integration_bo import IntegrationBO


class IntegrationCrudInputMappingServiceV1:

    def __call__(self, input_integration: IntegrationCrudInputV1) -> IntegrationBO:
        return IntegrationBO(**input_integration.model_dump())
