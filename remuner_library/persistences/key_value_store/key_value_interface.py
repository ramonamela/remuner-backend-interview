from abc import ABC, abstractmethod
from typing import Any


class KeyValueInterface(ABC):
    @abstractmethod
    def set(self, key: str, value: Any):
        pass

    @abstractmethod
    def set_if_not_exists(self, key: str, value: Any):
        pass

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def atomic_key_increment(self, key: str):
        pass

    @abstractmethod
    def atomic_key_decrement(self, key: str):
        pass
