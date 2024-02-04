from typing import Any

import aioredis

from app.config import redis_settings
from remuner_library.persistences.key_value_store.key_value_interface import KeyValueInterface


class RedisCache(KeyValueInterface):
    def __init__(self):
        self.redis = aioredis.Redis.from_url(
            f"redis://{redis_settings.host}/{redis_settings.database}", port=redis_settings.port
        )

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: Any):
        return await self.redis.set(key, value)

    async def set_if_not_exists(self, key: str, value: Any):
        return await self.redis.setnx(key, value)

    async def atomic_key_increment(self, key: str):
        return await self.redis.incr(key)

    async def atomic_key_decrement(self, key: str):
        return await self.redis.decr(key)
