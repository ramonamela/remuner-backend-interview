from app.users.application.view_controllers.v1.team.v1.common.input_mapping_service import (
    TeamCrudInputMappingServiceV1,
)
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudIdOutputV1,
    TeamCrudInputV1,
)


class UpdateTeamViewControllerV1:
    def __init__(self, input_mapping_service, team_bo_persistence_service):
        self.input_mapping_service: TeamCrudInputMappingServiceV1 = input_mapping_service
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, team_id: int, input_team: TeamCrudInputV1):
        input_team.id = team_id
        team_bo = self.input_mapping_service(input_team)
        await self.team_bo_persistence_service.update(team_bo=team_bo)
        return TeamCrudIdOutputV1(id=team_bo.id)
