from app.integrations.api.v1.integration.v1.common.view_models import IntegrationIdOutputV1
from app.integrations.dependency_injection.application.view_controllers.v1.integration.utilities.count import (
    CountIntegrationControllers,
)


async def integrations_count_get_v1() -> IntegrationIdOutputV1:
    view_controller = CountIntegrationControllers.v1()
    return await view_controller()
