from typing import List, Optional

from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus
from app.users.api.v1.user.v1.common.swagger_examples import post_input_v1
from app.users.enums import UserStatus


class UserInputV1(BaseModel):
    id: Optional[int] = None
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    teams: List[int] = None
    integrations: List[int] = None

    model_config = {"json_schema_extra": {"examples": [post_input_v1]}}


class UserTeamOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)


class UserIntegrationOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    status: IntegrationStatus


class UserOutputV1(BaseModel):
    id: int
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    status: UserStatus
    teams: List[UserTeamOutputV1]
    integrations: List[UserIntegrationOutputV1]


class UserIdOutputV1(BaseModel):
    id: int
