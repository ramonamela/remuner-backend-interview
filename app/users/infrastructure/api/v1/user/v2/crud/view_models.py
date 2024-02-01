from typing import List

from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v2.crud.swagger_examples import crud_post_input_v2


class UserCrudInputV2(BaseModel):
    name: str
    last_name: str
    email: str
    teams: List[int] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v2]}}


class UserCrudTeamOutputV2(BaseModel):
    id: int
    name: str


class UserCrudIntegrationOutputV2(BaseModel):
    id: int
    name: str
    status: IntegrationStatus


class UserCrudOutputV2(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    status: UserStatus
    teams: List[UserCrudTeamOutputV2]
    integrations: List[UserCrudIntegrationOutputV2]


class UserCrudIdOutputV2(BaseModel):
    id: int
