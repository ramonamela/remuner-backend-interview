from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.config import DATABASE_URL, models
from app.integrations.router import router as integrations_router
from app.users.router import router as users_router

app = FastAPI()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


# redis = await aioredis.create_redis(
#        f'redis://{redis_settings.host}',
#        port=redis_settings.port,
#        encoding='utf-8'
#    )
# await redis.set('my-key', 'value')
# val = await redis.get('my-key')
# print(val)

app.include_router(integrations_router, prefix="", tags=["Integrations"])
app.include_router(users_router, prefix="", tags=["Users"])

# Only allow origin where frontend is exposed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend's origin
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": models},
    generate_schemas=False,
    add_exception_handlers=True,
)
