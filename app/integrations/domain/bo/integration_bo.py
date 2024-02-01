from typing import Optional

from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.users.domain.bo.user_bo import UserBO
from app.users.enums import UserStatus


class IntegrationBO(BaseModel):
    id: Optional[int] = None
    name: str
    token: Optional[str] = None
    user: Optional[UserBO] = None
    user_id: int
    status: Optional[IntegrationStatus] = UserStatus.PENDING
