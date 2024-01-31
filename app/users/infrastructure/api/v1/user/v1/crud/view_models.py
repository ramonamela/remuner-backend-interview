from typing import List

from pydantic import BaseModel

from app.users.infrastructure.api.v1.user.v1.crud.swagger_examples import crud_post_input_v1


class UserCrudPostInputV1(BaseModel):
    first_name: str
    last_name: str
    email: str
    teams: List[int] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class UserCrudPostOutputV1(BaseModel):
    id: int
