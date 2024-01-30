from abc import ABC, abstractmethod

from app.users.domain.bo.team_bo import TeamBO


class TeamBOPersistenceInterface(ABC):
    @abstractmethod
    def create(self, team_bo: TeamBO):
        pass
