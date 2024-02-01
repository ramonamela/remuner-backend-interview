from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.integrations.infrastructure.api.v1.integration.v1.crud.swagger_examples import (
    crud_post_input_v1,
)


class IntegrationCrudInputV1(BaseModel):
    name: str
    token: str
    user_id: int

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class IntegrationCrudUserOutputV1(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class IntegrationCrudOutputV1(BaseModel):
    id: int
    name: str
    status: IntegrationStatus
    user_first_name: str
    user_last_name: str
    user_email: str


class IntegrationCrudIdOutputV1(BaseModel):
    id: int
