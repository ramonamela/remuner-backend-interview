from typing import List

from fastapi import HTTPException

from app.users.api.v1.user.v1.common.input_mapping_service import UserInputMappingServiceV1
from app.users.api.v1.user.v1.common.output_mapping_service import UserOutputMappingServiceV1
from app.users.api.v1.user.v1.common.view_models import UserIdOutputV1, UserInputV1, UserOutputV1
from app.users.dependency_injection.domain.controllers.v1.user.crud.create import (
    CreateUserControllers,
)
from app.users.dependency_injection.domain.controllers.v1.user.crud.delete import (
    DeleteUserControllers,
)
from app.users.dependency_injection.domain.controllers.v1.user.crud.get import (
    GetUserControllers,
)
from app.users.dependency_injection.domain.controllers.v1.user.crud.update import (
    UpdateUserControllers,
)
from app.users.domain.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.domain.persistence.exceptions.user_bo import (
    RepeatedEmailException,
    UserHasIntegrationsException,
    UserNotFoundException,
)


async def users_get_v1() -> List[UserOutputV1]:
    view_controller = GetUserControllers.v1()
    output_mapping_service = UserOutputMappingServiceV1()
    return [output_mapping_service(user_bo=user_bo) for user_bo in await view_controller()]


async def users__user_id_get_v1(user_id: int) -> UserOutputV1:
    view_controller = GetUserControllers.v1()
    output_mapping_service = UserOutputMappingServiceV1()
    return await output_mapping_service(user_bo=view_controller(user_id=user_id))


async def users_post_v1(post_input: UserInputV1) -> UserIdOutputV1:
    view_controller = CreateUserControllers.v1()
    input_mapping_service = UserInputMappingServiceV1()
    try:
        return UserIdOutputV1(id=await view_controller(user_bo=input_mapping_service(post_input)))
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def users__user_id_post_v1(user_id: int, post_input: UserInputV1) -> UserIdOutputV1:
    view_controller = UpdateUserControllers.v1()
    input_mapping_service = UserInputMappingServiceV1()
    try:
        return UserIdOutputV1(
            id=await view_controller(user_id=user_id, user_bo=input_mapping_service(post_input))
        )
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")


async def users__user_id_delete_v1(user_id: int):
    view_controller = DeleteUserControllers.v1()
    try:
        await view_controller(user_id=user_id)
        return {}
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")
    except UserHasIntegrationsException:
        raise HTTPException(status_code=403, detail="User has integrations")
