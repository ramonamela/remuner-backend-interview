from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudOutputV1,
    IntegrationCrudUserOutputV1,
)
from app.users.domain.bo.user_bo import UserBO


class IntegrationCrudOutputMappingServiceV1:

    def _get_user(self, user_bo: UserBO) -> IntegrationCrudUserOutputV1:
        return IntegrationCrudUserOutputV1(
            id=user_bo.id,
            first_name=user_bo.first_name,
            last_name=user_bo.last_name,
            email=user_bo.email,
            status=user_bo.status,
        )

    def __call__(self, integration_bo: IntegrationBO) -> IntegrationCrudOutputV1:
        return IntegrationCrudOutputV1(
            id=integration_bo.id,
            name=integration_bo.name,
            user_first_name=integration_bo.user.first_name,
            user_last_name=integration_bo.user.last_name,
            user_email=integration_bo.user.email,
            status=integration_bo.status,
        )
