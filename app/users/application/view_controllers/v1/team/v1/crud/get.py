from typing import List, Optional, Union

from app.users.application.view_controllers.v1.team.v1.common.output_mapping_service import (
    TeamCrudOutputMappingServiceV1,
)
from app.users.domain.persistence.team_bo_persistence_interface import TeamBOPersistenceInterface
from app.users.infrastructure.api.v1.team.v1.crud.view_models import TeamCrudOutputV1


class GetTeamViewControllerV1:
    def __init__(self, output_mapping_service, team_bo_persistence_service):
        self.output_mapping_service: TeamCrudOutputMappingServiceV1 = output_mapping_service
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(
        self, team_id: Optional[int] = None
    ) -> Union[TeamCrudOutputV1, List[TeamCrudOutputV1]]:
        if team_id is None:
            team_bos = await self.team_bo_persistence_service.get_all()
            return [self.output_mapping_service(team_bo=team_bo) for team_bo in team_bos]
        else:
            team_bo = await self.team_bo_persistence_service.get(team_id=team_id)
            return self.output_mapping_service(team_bo=team_bo)
