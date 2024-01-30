from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.user.crud.create import (
    CreateUserViewControllers,
)
from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudPostInputV1,
    UserCrudPostOutputV1,
)
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException


async def users_get_v1() -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_get_v1(user_id: int) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users_post_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    view_controller = CreateUserViewControllers.v1()
    try:
        return await view_controller(input_user=post_input)
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")


async def users_post_v2(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_post_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})


async def users__user_id_delete_v1(post_input: UserCrudPostInputV1) -> UserCrudPostOutputV1:
    return UserCrudPostOutputV1(**{"id": 1})
