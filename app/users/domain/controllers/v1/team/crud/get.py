from typing import List, Optional, Union

from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.persistence.interfaces.team_bo_persistence_interface import (
    TeamBOPersistenceInterface,
)


class GetTeamViewControllerV1:
    def __init__(self, team_bo_persistence_service):
        self.team_bo_persistence_service: TeamBOPersistenceInterface = team_bo_persistence_service

    async def __call__(self, team_id: Optional[int] = None) -> Union[TeamBO, List[TeamBO]]:
        if team_id is None:
            return await self.team_bo_persistence_service.get_all()
        else:
            return await self.team_bo_persistence_service.get(team_id=team_id)
