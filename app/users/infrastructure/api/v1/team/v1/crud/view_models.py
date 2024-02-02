from typing import List, Optional

from pydantic import BaseModel, Field

from app.users.infrastructure.api.v1.team.v1.crud.swagger_examples import crud_post_input_v1


class TeamCrudInputV1(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    users: List[int]

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class TeamCrudUserOutputV1(BaseModel):
    id: int
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)


class TeamCrudOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    users: List[TeamCrudUserOutputV1]


class TeamCrudIdOutputV1(BaseModel):
    id: int
