from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)


class CreateTeamControllerV1:
    def __init__(self, team_bo_persistence_service):
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, team_bo: TeamBO) -> int:
        return await self.team_bo_persistence_service.create(team_bo=team_bo)
