from typing import Any, List, Optional

from pydantic import BaseModel

from app.users.enums import UserStatus


class UserBO(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    status: Optional[UserStatus] = UserStatus.PENDING
    team_ids: Optional[List[int]] = None
    team: Optional[List[Any]] = None  # Trick to allow circular reference, this Any is indeed TeamBO
