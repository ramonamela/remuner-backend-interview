from pydantic import BaseModel


class IntegrationStatsOutputV1(BaseModel):
    count: int
