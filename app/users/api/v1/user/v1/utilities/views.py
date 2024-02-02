from app.users.api.v1.user.v1.utilities.view_models import UserStatsOutputV1
from app.users.dependency_injection.domain.controllers.v1.user.utilities.stats import (
    GetUsersStatsControllers,
)


async def users_stats_get_v1() -> UserStatsOutputV1:
    view_controller = GetUsersStatsControllers.v1()
    return UserStatsOutputV1(count=await view_controller())
