from app.users.application.view_controllers.v1.team.v1.common.input_mapping_service import (
    TeamCrudPostInputMappingServiceV1,
)
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudPostInputV1,
    TeamCrudPostOutputV1,
)


class CreateTeamViewControllerV1:
    def __init__(self, input_mapping_service, team_bo_persistence_service):
        self.input_mapping_service: TeamCrudPostInputMappingServiceV1 = input_mapping_service
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, input_team: TeamCrudPostInputV1):
        team_bo = self.input_mapping_service(input_team)
        await self.team_bo_persistence_service.create(team_bo=team_bo)
        return TeamCrudPostOutputV1(id=team_bo.id)
