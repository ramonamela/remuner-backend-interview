from typing import Optional

from pydantic import BaseModel, Field

from app.integrations.api.v1.integration.v1.crud.swagger_examples import (
    crud_post_input_v1,
)


class IntegrationCrudInputV1(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    token: Optional[str] = Field(None, min_length=1)
    user_id: int

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}
