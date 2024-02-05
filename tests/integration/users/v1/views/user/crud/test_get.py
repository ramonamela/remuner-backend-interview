import pytest
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value",
    [
        ("1", "first_name", 200),
        ("2", "name", 200),
        ("3", "name", 400),
    ],
)
async def test_get(client: TestClient, header, key, expected_value, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    resp = await client.get(
        "/v1/users/" + str(user_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        assert key in resp.json()
