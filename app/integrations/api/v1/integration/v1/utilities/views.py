from app.integrations.api.v1.integration.v1.utilities.view_models import IntegrationStatsOutputV1
from app.integrations.dependency_injection.domain.controllers.v1.integration.utilities.stats import (
    GetIntegrationsStatsControllers,
)


async def integrations_stats_get_v1() -> IntegrationStatsOutputV1:
    view_controller = GetIntegrationsStatsControllers.v1()
    return IntegrationStatsOutputV1(count=await view_controller())
