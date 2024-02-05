import pytest
from async_asgi_testclient import TestClient

from app.users.dependency_injection.persistence.user_bo import UserBOPersistenceServices


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, expected_value",
    [
        ("1", 200),
        ("2", 400),
    ],
)
async def test_delete(client: TestClient, header, expected_value, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    persistence_service = UserBOPersistenceServices.remuner()
    resp = await client.get(
        "/v1/users/stats",
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        assert resp.json()["count"] == 1
    await persistence_service.delete(user_id=user_bo.id)
    resp = await client.get(
        "/v1/users/stats",
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        assert resp.json()["count"] == 0
