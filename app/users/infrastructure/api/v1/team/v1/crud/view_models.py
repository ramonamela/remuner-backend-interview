from typing import List, Optional

from pydantic import BaseModel

from app.users.infrastructure.api.v1.team.v1.crud.swagger_examples import crud_post_input_v1


class TeamCrudInputV1(BaseModel):
    name: str
    users: Optional[List[int]] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class TeamCrudUserOutputV1(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class TeamCrudOutputV1(BaseModel):
    id: int
    name: str
    users: List[TeamCrudUserOutputV1]


class TeamCrudIdOutputV1(BaseModel):
    id: int
