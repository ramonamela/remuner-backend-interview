from pydantic import BaseModel


class UserStatsOutputV1(BaseModel):
    count: int
