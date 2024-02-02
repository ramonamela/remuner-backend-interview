from typing import List, Optional

from pydantic import BaseModel, Field

from app.users.api.v1.team.v1.common.swagger_examples import post_input_v1


class TeamInputV1(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    users: List[int]

    model_config = {"json_schema_extra": {"examples": [post_input_v1]}}


class TeamIdOutputV1(BaseModel):
    id: int
