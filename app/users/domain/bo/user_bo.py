from typing import Optional

from pydantic import BaseModel

from app.users.enums import UserStatus


class UserBO(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    status: Optional[UserStatus] = UserStatus.PENDING
