from typing import Union

from fastapi import APIRouter, Header, Response

from app.users.api.v1.user.v1.crud.view_models import UserCrudInputV1
from app.users.api.v1.user.v1.crud.views import (
    users__user_id_delete_v1,
    users__user_id_get_v1,
    users__user_id_post_v1,
    users_get_v1,
    users_post_v1,
)
from app.users.api.v1.user.v2.crud.view_models import UserCrudInputV2
from app.users.api.v1.user.v2.crud.views import (
    users__user_id_get_v2,
    users__user_id_post_v2,
    users_get_v2,
    users_post_v2,
)
from remuner_library.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.get("/users")
@custom_router_decorator(versions={"1": users_get_v1, "2": users_get_v2})
async def users_get(response: Response, X_API_Version: str = Header(None, enum=["1", "2"])):
    pass


@router.get("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_get_v1, "2": users__user_id_get_v2})
async def users__user_id_get(
    user_id: int, response: Response, X_API_Version: str = Header(None, enum=["1", "2"])
):
    pass


@router.post("/users")
@custom_router_decorator(versions={"1": users_post_v1, "2": users_post_v2})
async def users_post(
    post_input: Union[UserCrudInputV1, UserCrudInputV2],
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.post("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_post_v1, "2": users__user_id_post_v2})
async def users__user_id_post(
    user_id: int,
    post_input: Union[UserCrudInputV1, UserCrudInputV2],
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.delete("/users/{user_id}")
@custom_router_decorator(versions={"1": users__user_id_delete_v1})
async def users__user_id_delete(
    user_id: int, response: Response, X_API_Version: str = Header(None, enum=["1"])
):
    pass
