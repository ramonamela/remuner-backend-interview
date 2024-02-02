from typing import List

from fastapi import HTTPException

from app.users.api.v1.user.v2.common.input_mapping_service import UserInputMappingServiceV2
from app.users.api.v1.user.v2.common.output_mapping_service import UserOutputMappingServiceV2
from app.users.api.v1.user.v2.common.view_models import UserIdOutputV2, UserInputV2, UserOutputV2
from app.users.dependency_injection.domain.controllers.v1.user.crud.create import (
    CreateUserControllers,
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
    UserNotFoundException,
)


async def users_get_v2() -> List[UserOutputV2]:
    view_controller = GetUserControllers.v2()
    output_mapping_service = UserOutputMappingServiceV2()
    return [output_mapping_service(user_bo=user_bo) for user_bo in await view_controller()]


async def users__user_id_get_v2(user_id: int) -> UserOutputV2:
    view_controller = GetUserControllers.v2()
    output_mapping_service = UserOutputMappingServiceV2()
    return output_mapping_service(user_bo=await view_controller(user_id=user_id))


async def users_post_v2(post_input: UserInputV2) -> UserIdOutputV2:
    view_controller = CreateUserControllers.v1()
    input_mapping_service = UserInputMappingServiceV2()
    try:
        return await view_controller(user_bo=input_mapping_service(post_input))
    except RepeatedEmailException:
        raise HTTPException(status_code=409, detail="Email already exists in the database")
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def users__user_id_post_v2(user_id: int, post_input: UserInputV2) -> UserIdOutputV2:
    view_controller = UpdateUserControllers.v2()
    input_mapping_service = UserInputMappingServiceV2()
    try:
        return await view_controller(user_id=user_id, user_bo=input_mapping_service(post_input))
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")
