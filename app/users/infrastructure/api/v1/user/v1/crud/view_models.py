from typing import List, Optional

from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v1.crud.swagger_examples import crud_post_input_v1


class UserCrudInputV1(BaseModel):
    id: Optional[int] = None
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    teams: List[int] = None
    integrations: List[int] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class UserCrudTeamOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)


class UserCrudIntegrationOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    status: IntegrationStatus


class UserCrudOutputV1(BaseModel):
    id: int
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    status: UserStatus
    teams: List[UserCrudTeamOutputV1]
    integrations: List[UserCrudIntegrationOutputV1]


class UserCrudIdOutputV1(BaseModel):
    id: int
