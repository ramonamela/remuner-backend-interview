import asyncio
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from async_asgi_testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.config import DATABASE_URL, models
from app.main import app


@pytest.fixture(autouse=True, scope="session")
def run_migrations() -> None:
    import os

    print("running migrations..")
    os.system("alembic upgrade head")
    yield
    os.system("alembic downgrade base")


@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def client(db) -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "9500"
    scope = {"client": (host, port)}

    async with TestClient(app, scope=scope) as client:
        yield client


@pytest_asyncio.fixture
def db():
    initializer(
        db_url=DATABASE_URL,
        modules=models,
    )
    yield
    finalizer()
