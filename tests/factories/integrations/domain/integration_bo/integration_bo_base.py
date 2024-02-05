import pytest
from factory import Factory

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.integrations.enums import IntegrationStatus


class IntegrationBOFactory(Factory):

    class Meta:
        model = IntegrationBO

    name = "RemunerIntegration"
    token = "RemunerToken"
    user = None
    user_id = 1
    status = IntegrationStatus.ACTIVE


@pytest.fixture
async def integration_bo_factory_db(user_bo_factory_db):
    user_bo = await user_bo_factory_db
    persistence_service = IntegrationBOPersistenceServices.remuner()
    integration_bo = IntegrationBOFactory(user_id=user_bo.id)
    await persistence_service.create(integration_bo)
    return integration_bo
