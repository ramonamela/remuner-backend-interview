from abc import ABC, abstractmethod
from typing import List

from app.users.domain.bo.team_bo import TeamBO


class TeamBOPersistenceInterface(ABC):
    @abstractmethod
    def create(self, team_bo: TeamBO):
        pass

    @abstractmethod
    async def update(self, team_bo: TeamBO) -> id:
        pass

    @abstractmethod
    async def get_all(self) -> List[TeamBO]:
        pass

    @abstractmethod
    async def get(self, team_id: int) -> TeamBO:
        pass

    @abstractmethod
    async def delete(self, team_id: int):
        pass

    @abstractmethod
    async def count_elements(self):
        pass
