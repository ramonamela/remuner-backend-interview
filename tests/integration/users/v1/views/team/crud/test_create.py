import pytest
from async_asgi_testclient import TestClient

from app.users.api.v1.team.v1.common.swagger_examples import post_input_v1
from app.users.dependency_injection.persistence.team_bo import TeamBOPersistenceServices


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value", [("1", "name", 200), ("2", "name", 400), ("1", "random", 422)]
)
async def test_create(client: TestClient, header, key, expected_value) -> None:
    resp = await client.post(
        "/v1/teams",
        json={
            key: "test_team" + str(header),
            "users": [],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value


@pytest.mark.asyncio
async def test_create_swagger(client: TestClient) -> None:
    resp = await client.post("/v1/teams", json=post_input_v1, headers={"X-API-Version": "1"})
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_create_repeated(client: TestClient) -> None:
    resp = await client.post(
        "/v1/teams",
        json={"name": "test_team1", "users": []},
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 200

    resp = await client.post(
        "/v1/teams",
        json={"name": "test_team1", "users": []},
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_create_with_user(client: TestClient, user_bo_factory_db):
    user_bo = await user_bo_factory_db
    team_bo_persistence_service = TeamBOPersistenceServices.remuner()
    resp = await client.post(
        "/v1/teams",
        json={
            "name": "RemunerTeam",
            "users": [user_bo.id],
        },
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 200
    persisted_team_bo = await team_bo_persistence_service.get(team_id=resp.json()["id"])
    assert set(persisted_team_bo.user_ids) == {user_bo.id}
