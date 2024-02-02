from typing import List, Optional

from pydantic import BaseModel, Field

from app.users.domain.bo.user_bo import UserBO


class TeamBO(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1)
    user_ids: Optional[List[int]] = None
    users: Optional[List[UserBO]] = None
