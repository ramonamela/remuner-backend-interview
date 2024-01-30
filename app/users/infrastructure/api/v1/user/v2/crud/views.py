from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.user.crud.create import (
    CreateUserViewControllers,
)
from app.users.infrastructure.api.v1.user.v2.crud.view_models import (
    UserCrudPostInputV2,
    UserCrudPostOutputV2,
)
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException


async def users_post_v2(post_input: UserCrudPostInputV2) -> UserCrudPostOutputV2:
    view_controller = CreateUserViewControllers.v2()
    try:
        return await view_controller(input_user=post_input)
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")


async def users__user_id_post_v2(post_input: UserCrudPostInputV2) -> UserCrudPostOutputV2:
    raise Exception
    return UserCrudPostOutputV2(**{"id": 1})
