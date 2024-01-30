from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.users.infrastructure.api.v1.team.v1.crud.swagger_examples import crud_post_input_v1


class IntegrationCrudPostInputV1(BaseModel):
    name: str
    token: str
    user_id: int
    status: IntegrationStatus

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class IntegrationCrudPostOutputV1(BaseModel):
    id: int
