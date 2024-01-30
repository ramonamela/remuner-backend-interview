from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.integrations.router import router as integrations_router
from app.users.router import router as users_router
from app.config import DATABASE_URL, models

app = FastAPI()

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(integrations_router, prefix="/integrations", tags=["Integrations"])
app.include_router(users_router, prefix="", tags=["Users"])

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": models},
    generate_schemas=False,
    add_exception_handlers=True,
)
