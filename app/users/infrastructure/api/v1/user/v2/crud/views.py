from app.users.infrastructure.api.v1.user.v1.crud.view_models import UserCrudPostOutputV1
from app.users.infrastructure.api.v1.user.v2.crud.view_models import UserCrudPostInputV2


async def users_post_v2(post_input: UserCrudPostInputV2) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 2})
