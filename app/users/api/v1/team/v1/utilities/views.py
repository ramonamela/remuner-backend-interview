from app.users.api.v1.team.v1.utilities.view_models import TeamStatsOutputV1
from app.users.dependency_injection.domain.controllers.v1.team.utilities.stats import (
    GetTeamsStatsControllers,
)


async def teams_stats_get_v1() -> TeamStatsOutputV1:
    view_controller = GetTeamsStatsControllers.v1()
    return TeamStatsOutputV1(count=await view_controller())
