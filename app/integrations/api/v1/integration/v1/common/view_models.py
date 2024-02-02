from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus


class IntegrationIdOutputV1(BaseModel):
    id: int


class IntegrationOutputV1(BaseModel):
    id: int
    name: str = Field(min_length=1)
    status: IntegrationStatus
    user_first_name: str = Field(min_length=1)
    user_last_name: str = Field(min_length=1)
    user_email: str = Field(min_length=1)
