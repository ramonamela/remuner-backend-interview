from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudPostInputV1,
    UserCrudPostOutputV1,
)


async def users_get_v1() -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_get_v1(user_id: int) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users_post_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users_post_v2(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_post_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_post_v2(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_delete_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})
