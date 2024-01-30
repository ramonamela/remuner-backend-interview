from pydantic import BaseModel

from app.users.infrastructure.api.v1.user.v2.crud.swagger_examples import crud_post_input_v2


class UserCrudPostInputV2(BaseModel):
    name: str
    last_name: str
    email: str

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v2]}}


class UserCrudPostOutputV2(BaseModel):
    id: int
