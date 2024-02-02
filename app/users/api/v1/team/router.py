from fastapi import APIRouter, Header, Response

from app.users.api.v1.team.v1.common.view_models import TeamInputV1
from app.users.api.v1.team.v1.crud.views import (
    teams__team_id_delete_v1,
    teams__team_id_get_v1,
    teams__team_id_post_v1,
    teams_get_v1,
    teams_post_v1,
)
from app.users.api.v1.team.v1.utilities.views import teams_stats_get_v1
from remuner_library.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.post("/teams")
@custom_router_decorator(versions={"1": teams_post_v1})
async def teams_post(
    post_input: TeamInputV1,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.get("/teams/stats")
@custom_router_decorator(versions={"1": teams_stats_get_v1})
async def teams_stats_get(response: Response, X_API_Version: str = Header(None, enum=["1"])):
    pass


@router.get("/teams")
@custom_router_decorator(versions={"1": teams_get_v1})
async def teams_get(
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.get("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_get_v1})
async def teams__team_id_get(
    team_id: int,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.post("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_post_v1})
async def teams__team_id_post(
    team_id: int,
    post_input: TeamInputV1,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.delete("/teams/{team_id}")
@custom_router_decorator(versions={"1": teams__team_id_delete_v1})
async def teams__team_id_delete(
    team_id: int,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass
