from typing import List, Optional

from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus
from app.users.api.v1.user.v2.common.swagger_examples import crud_post_input_v2
from app.users.enums import UserStatus


class UserInputV2(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    teams: List[int] = None
    integrations: List[int] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v2]}}


class UserTeamOutputV2(BaseModel):
    id: int
    name: str = Field(min_length=1)


class UserIntegrationOutputV2(BaseModel):
    id: int
    name: str = Field(min_length=1)
    status: IntegrationStatus


class UserOutputV2(BaseModel):
    id: int
    name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    status: UserStatus
    teams: List[UserTeamOutputV2]
    integrations: List[UserIntegrationOutputV2]


class UserIdOutputV2(BaseModel):
    id: int
