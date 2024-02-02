from typing import List

from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.user.crud.create import (
    CreateUserViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.user.crud.delete import (
    DeleteUserViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.user.crud.get import (
    GetUserViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.user.crud.update import (
    UpdateUserViewControllers,
)
from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudIdOutputV1,
    UserCrudInputV1,
    UserCrudOutputV1,
)
from app.users.infrastructure.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.infrastructure.persistence.exceptions.user_bo import (
    RepeatedEmailException,
    UserHasIntegrationsException,
    UserNotFoundException,
)


async def users_get_v1() -> List[UserCrudOutputV1]:
    view_controller = GetUserViewControllers.v1()
    return await view_controller()


async def users__user_id_get_v1(user_id: int) -> UserCrudIdOutputV1:
    view_controller = GetUserViewControllers.v1()
    return await view_controller(user_id=user_id)


async def users_post_v1(post_input: UserCrudInputV1) -> UserCrudIdOutputV1:
    view_controller = CreateUserViewControllers.v1()
    try:
        return await view_controller(input_user=post_input)
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def users__user_id_post_v1(user_id: int, post_input: UserCrudInputV1) -> UserCrudIdOutputV1:
    view_controller = UpdateUserViewControllers.v1()
    try:
        return await view_controller(user_id=user_id, input_user=post_input)
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")


async def users__user_id_delete_v1(user_id: int) -> UserCrudIdOutputV1:
    view_controller = DeleteUserViewControllers.v1()
    try:
        return await view_controller(user_id=user_id)
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")
    except UserHasIntegrationsException:
        raise HTTPException(status_code=403, detail="User has integrations")
