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
async def test_get(client: TestClient, header, expected_value, team_bo_factory_db) -> None:
    team_bo = await team_bo_factory_db
    resp = await client.get(
        "/v1/teams/" + str(team_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        assert resp.json()["name"] == team_bo.name
