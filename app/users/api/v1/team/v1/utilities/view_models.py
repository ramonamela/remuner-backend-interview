from pydantic import BaseModel


class TeamStatsOutputV1(BaseModel):
    count: int
