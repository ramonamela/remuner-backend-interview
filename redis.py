import aioredis

from app.config import redis_settings


async def redis_pool_init():
    return await aioredis.create_redis_pool(
        f"redis://{redis_settings.host}", port=redis_settings.port
    )


redis_pool = redis_pool_init()
