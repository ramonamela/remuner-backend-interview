import pytest
from async_asgi_testclient import TestClient

from app.users.dependency_injection.persistence.user_bo import UserBOPersistenceServices


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value",
    [
        ("1", "first_name", 200),
        ("2", "name", 200),
        ("3", "name", 400),
    ],
)
async def test_update(client: TestClient, header, key, expected_value, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    resp = await client.post(
        "/v1/users/" + str(user_bo.id),
        json={
            key: "NewName",
            "last_name": user_bo.last_name,
            "email": user_bo.email,
            "teams": user_bo.team_ids,
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    if expected_value == 200:
        persistence_service = UserBOPersistenceServices.remuner()
        persisted_user_bo = await persistence_service.get(user_id=user_bo.id)
        assert persisted_user_bo.first_name == "NewName"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value",
    [
        ("1", "first_name", 200),
        ("2", "name", 200),
    ],
)
async def test_update_with_team(
    client: TestClient, header, key, expected_value, user_bo_factory_db, team_bo_factory_db
) -> None:
    user_bo = await user_bo_factory_db
    team_bo = await team_bo_factory_db
    resp = await client.post(
        "/v1/users/" + str(user_bo.id),
        json={
            key: "NewName",
            "last_name": user_bo.last_name,
            "email": user_bo.email,
            "teams": [team_bo.id],
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    persistence_service = UserBOPersistenceServices.remuner()
    persisted_user_bo = await persistence_service.get(user_id=user_bo.id)
    assert persisted_user_bo.first_name == "NewName"
    assert set(persisted_user_bo.team_ids) == {team_bo.id}
