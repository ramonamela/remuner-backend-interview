import pytest
from async_asgi_testclient import TestClient


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, expected_value",
    [
        ("1", 200),
        ("2", 400),
    ],
)
async def test_get(client: TestClient, header, expected_value, integration_bo_factory_db) -> None:
    integration_bo = await integration_bo_factory_db
    resp = await client.get(
        "/v1/integrations/" + str(integration_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        assert resp.json()["name"] == integration_bo.name
