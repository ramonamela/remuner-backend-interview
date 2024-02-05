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
async def test_update(client: TestClient, header, expected_value, team_bo_factory_db) -> None:
    team_bo = await team_bo_factory_db
    resp = await client.post(
        "/v1/teams/" + str(team_bo.id),
        json={"name": "NewName", "users": team_bo.user_ids},
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        persistence_service = TeamBOPersistenceServices.remuner()
        persisted_team_bo = await persistence_service.get(team_id=team_bo.id)
        assert persisted_team_bo.name == "NewName"


@pytest.mark.asyncio
async def test_update_with_user(client: TestClient, user_bo_factory_db, team_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    team_bo = await team_bo_factory_db
    resp = await client.post(
        "/v1/teams/" + str(user_bo.id),
        json={
            "name": "NewName",
            "users": [user_bo.id],
        },
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 200
    persistence_service = TeamBOPersistenceServices.remuner()
    persisted_team_bo = await persistence_service.get(team_id=team_bo.id)
    assert persisted_team_bo.name == "NewName"
    assert set(persisted_team_bo.user_ids) == {user_bo.id}
