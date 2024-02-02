from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)


class UpdateTeamControllerV1:
    def __init__(self, input_mapping_service, team_bo_persistence_service):
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, team_id: int, team_bo: TeamBO):
        team_bo.id = team_id
        return await self.team_bo_persistence_service.update(team_bo=team_bo)
