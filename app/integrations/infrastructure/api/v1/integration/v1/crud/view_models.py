from typing import Optional

from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus
from app.integrations.infrastructure.api.v1.integration.v1.crud.swagger_examples import (
    crud_post_input_v1,
)


class IntegrationCrudInputV1(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    token: Optional[str] = Field(None, min_length=1)
    user_id: int

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class IntegrationCrudUserOutputV1(BaseModel):
    id: int
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)


class IntegrationCrudOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    status: IntegrationStatus
    user_first_name: str = Field(min_length=1)
    user_last_name: str = Field(min_length=1)
    user_email: str = Field(min_length=1)


class IntegrationCrudIdOutputV1(BaseModel):
    id: int
