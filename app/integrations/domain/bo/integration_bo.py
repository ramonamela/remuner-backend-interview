from typing import Optional

from pydantic import BaseModel, Field

from app.integrations.enums import IntegrationStatus
from app.users.domain.bo.user_bo import UserBO
from app.users.enums import UserStatus


class IntegrationBO(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    token: Optional[str] = None
    user: Optional[UserBO] = None
    user_id: int
    status: Optional[IntegrationStatus] = UserStatus.PENDING
