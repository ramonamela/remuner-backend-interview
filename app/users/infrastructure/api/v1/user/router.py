from fastapi import APIRouter, Header, Response

from app.users.infrastructure.api.v1.user.v1.crud.views import users_post_v1, users_post_v2
from remuner_library.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.get("/users")
async def users_get():
    return {"message": "Users get"}


@router.get("/users/{user_id}")
async def users__user_id_get():
    return {"message": "Users id get"}


@router.post("/users")
@custom_router_decorator(
    versions={"1": users_post_v1, "2": users_post_v2},
)
async def users_post(
    post_input,
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.post("/users/{user_id}")
async def users__user_id_post():
    return {"message": "Users id post"}


@router.delete("/users/{user_id}")
async def users__user_id_delete():
    return {"message": "Users id delete"}
