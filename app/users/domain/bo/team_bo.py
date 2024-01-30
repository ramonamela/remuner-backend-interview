from typing import List, Optional

from pydantic import BaseModel

from app.users.domain.bo.user_bo import UserBO


class TeamBO(BaseModel):
    id: Optional[int] = None
    name: str
    user_ids: Optional[List[int]] = None
    users: Optional[List[UserBO]] = None
