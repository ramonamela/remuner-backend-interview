from typing import List, Union

from fastapi import APIRouter, Header, Response

from app.users.api.v1.user.v1.common.view_models import UserIdOutputV1, UserInputV1, UserOutputV1
from app.users.api.v1.user.v1.crud.views import (
    users__user_id_delete_v1,
    users__user_id_get_v1,
    users__user_id_post_v1,
    users_get_v1,
    users_post_v1,
)
from app.users.api.v1.user.v1.utilities.views import users_stats_get_v1
from app.users.api.v1.user.v2.common.view_models import UserInputV2, UserOutputV2
from app.users.api.v1.user.v2.crud.views import (
    users__user_id_get_v2,
    users__user_id_post_v2,
    users_get_v2,
    users_post_v2,
)
from remuner_library.fast_api_extension.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.post("/users")
@custom_router_decorator(versions={"1": users_post_v1, "2": users_post_v2})
async def users_post(
    post_input: Union[UserInputV1, UserInputV2],
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
) -> UserIdOutputV1:
    pass


@router.get("/users/stats")
@custom_router_decorator(versions={"1": users_stats_get_v1})
async def users_stats_get(response: Response, X_API_Version: str = Header(None, enum=["1"])):
    pass


@router.get("/users")
@custom_router_decorator(versions={"1": users_get_v1, "2": users_get_v2})
async def users_get(
    response: Response, X_API_Version: str = Header(None, enum=["1", "2"])
) -> Union[List[UserOutputV1], List[UserOutputV2]]:
    pass


@router.get("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_get_v1, "2": users__user_id_get_v2})
async def users__user_id_get(
    user_id: int, response: Response, X_API_Version: str = Header(None, enum=["1", "2"])
) -> Union[UserOutputV1, UserOutputV2]:
    pass


@router.post("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_post_v1, "2": users__user_id_post_v2})
async def users__user_id_post(
    user_id: int,
    post_input: Union[UserInputV1, UserInputV2],
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
) -> UserIdOutputV1:
    pass


@router.delete("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_delete_v1})
async def users__user_id_delete(
    user_id: int, response: Response, X_API_Version: str = Header(None, enum=["1"])
):
    pass
