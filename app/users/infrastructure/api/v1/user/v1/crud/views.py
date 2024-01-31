from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.user.crud.create import (
    CreateUserViewControllers,
)
from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudInputV1,
    UserCrudIdOutputV1,
)
from app.users.infrastructure.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException


async def users_get_v1() -> UserCrudIdOutputV1:
    return UserCrudIdOutputV1(**{"id": 1})


async def users__user_id_get_v1(user_id: int) -> UserCrudIdOutputV1:
    return UserCrudIdOutputV1(**{"id": 1})


async def users_post_v1(post_input: UserCrudInputV1) -> UserCrudIdOutputV1:
    view_controller = CreateUserViewControllers.v1()
    try:
        return await view_controller(input_user=post_input)
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def users__user_id_post_v1(post_input: UserCrudInputV1) -> UserCrudIdOutputV1:
    return UserCrudIdOutputV1(**{"id": 1})


async def users__user_id_delete_v1(post_input: UserCrudInputV1) -> UserCrudIdOutputV1:
    return UserCrudIdOutputV1(**{"id": 1})
