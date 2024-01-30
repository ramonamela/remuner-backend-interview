from typing import Optional

from pydantic import BaseModel


class TeamBO(BaseModel):
    id: Optional[int] = None
    name: str
