from typing import Any, List, Optional

from pydantic import BaseModel, Field

from app.users.enums import UserStatus


class UserBO(BaseModel):
    id: Optional[int] = None
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    status: Optional[UserStatus] = UserStatus.PENDING
    team_ids: Optional[List[int]] = None
    teams: Optional[List[Any]] = None  # Any to allow circular reference, this Any is indeed TeamBO
    integrations: Optional[List[Any]] = (
        None  # Any to allow circular reference, this Any is indeed IntegrationBO
    )
