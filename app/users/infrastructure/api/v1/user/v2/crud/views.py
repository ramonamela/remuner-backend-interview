from app.users.infrastructure.api.v1.user.v2.crud.view_models import (
    UserCrudPostInputV2,
    UserCrudPostOutputV2,
)


async def users_post_v2(post_input: UserCrudPostInputV2) -> UserCrudPostOutputV2:
    raise Exception
    return UserCrudPostOutputV2(**{"id": 2})


async def users__user_id_post_v2(post_input: UserCrudPostInputV2) -> UserCrudPostOutputV2:
    raise Exception
    return UserCrudPostOutputV2(**{"id": 1})
