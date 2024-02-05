import pytest
from async_asgi_testclient import TestClient

from app.users.api.v1.user.v1.common.swagger_examples import post_input_v1
from app.users.api.v1.user.v2.common.swagger_examples import post_input_v2
from app.users.dependency_injection.persistence.user_bo import UserBOPersistenceServices


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value",
    [
        ("1", "first_name", 200),
        ("2", "name", 200),
        ("3", "name", 400),
        ("1", "random", 422),
        ("2", "random", 422),
    ],
)
async def test_create(client: TestClient, header, key, expected_value) -> None:
    resp = await client.post(
        "/v1/users",
        json={
            key: "Ramon",
            "last_name": "Amela",
            "email": "ramonamela@gmail.com",
            "teams": [],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value


@pytest.mark.asyncio
@pytest.mark.parametrize("version, body", [("1", post_input_v1), ("2", post_input_v2)])
async def test_create_swagger(client: TestClient, version, body) -> None:
    resp = await client.post("/v1/users", json=post_input_v1, headers={"X-API-Version": "1"})
    assert resp.status_code == 200


@pytest.mark.asyncio
@pytest.mark.parametrize("header, key", [("1", "first_name"), ("2", "name")])
async def test_create_repeated(client: TestClient, header, key) -> None:
    resp = await client.post(
        "/v1/users",
        json={
            key: "Ramon",
            "last_name": "Amela",
            "email": "ramonamela@gmail.com",
            "teams": [],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == 200

    resp = await client.post(
        "/v1/users",
        json={
            key: "Ramon",
            "last_name": "Amela",
            "email": "ramonamela@gmail.com",
            "teams": [],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == 409


@pytest.mark.asyncio
@pytest.mark.parametrize("header, key", [("1", "first_name"), ("2", "name")])
async def test_create_with_team(client: TestClient, header, key, team_bo_factory_db):
    team_bo = await team_bo_factory_db
    user_bo_persistence_service = UserBOPersistenceServices.remuner()
    resp = await client.post(
        "/v1/users",
        json={
            key: "Ramon",
            "last_name": "Amela",
            "email": "ramonamela@gmail.com",
            "teams": [team_bo.id],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == 200
    persisted_user_bo = await user_bo_persistence_service.get(user_id=resp.json()["id"])
    assert set(persisted_user_bo.team_ids) == {team_bo.id}
