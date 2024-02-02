from typing import List

from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.users.enums import UserStatus
from app.users.infrastructure.api.v1.user.v1.crud.swagger_examples import crud_post_input_v1


class UserCrudInputV1(BaseModel):
    first_name: str
    last_name: str
    email: str
    teams: List[int] = None
    integrations: List[int] = None

    model_config = {"json_schema_extra": {"examples": [crud_post_input_v1]}}


class UserCrudTeamOutputV1(BaseModel):
    id: int
    name: str


class UserCrudIntegrationOutputV1(BaseModel):
    id: int
    name: str
    status: IntegrationStatus


class UserCrudOutputV1(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    status: UserStatus
    teams: List[UserCrudTeamOutputV1]
    integrations: List[UserCrudIntegrationOutputV1]


class UserCrudIdOutputV1(BaseModel):
    id: int
