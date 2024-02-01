from fastapi import APIRouter, Header, Response

from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudInputV1,
)
from app.integrations.infrastructure.api.v1.integration.v1.crud.views import (
    integrations__integration_id_delete_v1,
    integrations__integration_id_get_v1,
    integrations__integration_id_post_v1,
    integrations_get_v1,
    integrations_post_v1,
)
from remuner_library.fastapi_extensions import custom_router_decorator

router = APIRouter()


@router.get("/integrations")
@custom_router_decorator(versions={"1": integrations_get_v1})
async def integrations_get(response: Response, X_API_Version: str = Header(None, enum=["1"])):
    pass


@router.get("/integrations/{integration_id}")
@custom_router_decorator(versions={"1": integrations__integration_id_get_v1})
async def integrations__integration_id_get(
    integration_id: int, response: Response, X_API_Version: str = Header(None, enum=["1"])
):
    pass


@router.post("/integrations")
@custom_router_decorator(versions={"1": integrations_post_v1})
async def integrations_post(
    post_input: IntegrationCrudInputV1,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.post("/integrations/{integration_id}")
@custom_router_decorator(versions={"1": integrations__integration_id_post_v1})
async def integrations__integration_id_post(
    integration_id: int,
    response: Response,
    X_API_Version: str = Header(None, enum=["1"]),
):
    pass


@router.delete("/integrations/{integration_id}")
@custom_router_decorator(versions={"1": integrations__integration_id_delete_v1})
async def integrations__integration_id_delete(
    integration_id: int, response: Response, X_API_Version: str = Header(None, enum=["1"])
):
    pass
