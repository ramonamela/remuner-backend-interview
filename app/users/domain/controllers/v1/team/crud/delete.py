from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)


class DeleteTeamViewControllerV1:
    def __init__(self, team_bo_persistence_service):
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, team_id: int):
        await self.team_bo_persistence_service.delete(team_id=team_id)
