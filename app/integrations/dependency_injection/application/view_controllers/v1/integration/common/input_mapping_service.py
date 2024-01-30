from app.integrations.domain.bo.user_bo import IntegrationBO
from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudPostInputV1,
)


class IntegrationCrudPostInputMappingServiceV1:

    def __call__(self, input_team: IntegrationCrudPostInputV1):
        return IntegrationBO(**input_team.model_dump())
