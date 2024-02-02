from abc import ABC, abstractmethod

from app.users.domain.bo.user_bo import UserBO


class UserBOPersistenceInterface(ABC):
    @abstractmethod
    def create(self, user_bo: UserBO):
        pass
