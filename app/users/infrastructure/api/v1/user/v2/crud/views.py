from typing import List

from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.user.crud.create import (
    CreateUserViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.user.crud.get import (
    GetUserViewControllers,
)
from app.users.infrastructure.api.v1.user.v2.crud.view_models import (
    UserCrudIdOutputV2,
    UserCrudPostInputV2,
)
from app.users.infrastructure.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException


async def users_get_v2() -> UserCrudIdOutputV2:
    view_controller = GetUserViewControllers.v2()
    return await view_controller()


async def users__user_id_get_v2(user_id: int) -> List[UserCrudIdOutputV2]:
    view_controller = GetUserViewControllers.v2()
    return await view_controller(user_id=user_id)


async def users_post_v2(post_input: UserCrudPostInputV2) -> UserCrudIdOutputV2:
    view_controller = CreateUserViewControllers.v2()
    try:
        return await view_controller(input_user=post_input)
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def users__user_id_post_v2(post_input: UserCrudPostInputV2) -> UserCrudIdOutputV2:
    raise Exception
    return UserCrudIdOutputV2(**{"id": 1})
