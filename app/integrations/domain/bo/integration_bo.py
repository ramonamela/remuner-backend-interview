from typing import Optional

from pydantic import BaseModel

from app.integrations.enums import IntegrationStatus
from app.users.domain.bo.user_bo import UserBO


class IntegrationBO(BaseModel):
    id: Optional[int] = None
    name: str
    token: str
    user: UserBO
    status: IntegrationStatus
