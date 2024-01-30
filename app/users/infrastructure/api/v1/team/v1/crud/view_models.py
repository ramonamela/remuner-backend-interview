from pydantic import BaseModel
from typing import List, Optional

from app.users.infrastructure.api.v1.team.v1.crud.swagger_examples import crud_post_input_v1


class TeamCrudPostInputV1(BaseModel):
    name: str
    users: Optional[List[int]] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class TeamCrudPostOutputV1(BaseModel):
    id: int
