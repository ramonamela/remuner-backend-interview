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
    user_bos = await persistence_service.get_all()
    assert len(user_bos) == 1
    resp = await client.delete(
        "/v1/users/" + str(user_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    user_bos = await persistence_service.get_all()
    if expected_value == 200:
        assert len(user_bos) == 0

