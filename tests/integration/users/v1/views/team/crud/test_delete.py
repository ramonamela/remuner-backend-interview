import pytest
from async_asgi_testclient import TestClient

from app.users.dependency_injection.persistence.team_bo import TeamBOPersistenceServices


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, expected_value",
    [
        ("1", 200),
        ("2", 400),
    ],
)
async def test_delete(client: TestClient, header, expected_value, team_bo_factory_db) -> None:
    team_bo = await team_bo_factory_db
    persistence_service = TeamBOPersistenceServices.remuner()
    team_bos = await persistence_service.get_all()
    assert len(team_bos) == 1
    resp = await client.delete(
        "/v1/teams/" + str(team_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    team_bos = await persistence_service.get_all()
    if expected_value == 200:
        assert len(team_bos) == 0
