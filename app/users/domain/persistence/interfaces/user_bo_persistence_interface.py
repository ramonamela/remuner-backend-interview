from abc import ABC, abstractmethod
from typing import List

from app.users.domain.bo.user_bo import UserBO


class UserBOPersistenceInterface(ABC):
    @abstractmethod
    def create(self, user_bo: UserBO):
        pass

    @abstractmethod
    async def update(self, user_bo: UserBO) -> int:
        pass

    @abstractmethod
    async def get_all(self) -> List[UserBO]:
        pass

    @abstractmethod
    async def get_users_in(self, user_ids: List[int]):
        pass

    @abstractmethod
    async def get(self, user_id: int) -> UserBO:
        pass

    @abstractmethod
    async def delete(self, user_id: int):
        pass

    @abstractmethod
    async def count_elements(self):
        pass
