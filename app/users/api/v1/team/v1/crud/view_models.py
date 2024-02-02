from typing import List

from pydantic import BaseModel, Field


class TeamCrudUserOutputV1(BaseModel):
    id: int
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)


class TeamCrudOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    users: List[TeamCrudUserOutputV1]
