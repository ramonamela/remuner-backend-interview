from fastapi import APIRouter, Header, Response

from app.users.infrastructure.api.v1.team.v1.crud.view_models import TeamCrudPostInputV1
from app.users.infrastructure.api.v1.team.v1.crud.views import (
    teams__team_id_delete_v1,
    teams__team_id_get_v1,
    teams__team_id_post_v1,
    teams_get_v1,
    teams_post_v1,
)
from remuner_library.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.get("/teams")
@custom_router_decorator(versions={"1": teams_get_v1})
@custom_router_decorator
async def teams_get(
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.get("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_get_v1})
async def teams__team_id_get(
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.post("/teams")
@custom_router_decorator(versions={"1": teams_post_v1})
async def teams_post(
    post_input: TeamCrudPostInputV1,
    response: Response,
    X_API_Version: str = Header(None, enum=["1", "2"]),
):
    pass


@router.post("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_post_v1})
async def teams__team_id_post():
    pass


@router.delete("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_delete_v1})
async def teams__team_id_delete():
    pass
