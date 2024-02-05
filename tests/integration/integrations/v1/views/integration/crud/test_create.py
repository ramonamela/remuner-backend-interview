import pytest
from async_asgi_testclient import TestClient

from app.integrations.api.v1.integration.v1.crud.swagger_examples import crud_post_input_v1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value", [("1", "name", 200), ("2", "name", 400), ("1", "random", 422)]
)
async def test_create(client: TestClient, header, key, expected_value, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    resp = await client.post(
        "/v1/integrations",
        json={
            key: "test_team",
            "token": "random_token",
            "user_id": user_bo.id,
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value


@pytest.mark.asyncio
async def test_create_swagger(client: TestClient, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    crud_post_input_v1["user_id"] = user_bo.id
    resp = await client.post(
        "/v1/integrations", json=crud_post_input_v1, headers={"X-API-Version": "1"}
    )
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_create_repeated(client: TestClient, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    resp = await client.post(
        "/v1/integrations",
        json={"name": "test_integration", "token": "random_token", "user_id": user_bo.id},
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 200

    resp = await client.post(
        "/v1/integrations",
        json={"name": "test_integration", "token": "random_token", "user_id": user_bo.id},
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_create_in_users(client: TestClient, user_bo_factory_db) -> None:
    user_bo = await user_bo_factory_db
    resp_integrations = await client.post(
        "/v1/integrations",
        json={
            "name": "test_team",
            "token": "random_token",
            "user_id": user_bo.id,
        },
        headers={"X-API-Version": "1"},
    )
    assert resp_integrations.status_code == 200
    resp_users = await client.get(
        "/v1/users/" + str(user_bo.id),
        headers={"X-API-Version": "1"},
    )
    assert (
        len(
            list(
                filter(
                    lambda integration: integration["id"] == resp_integrations.json()["id"],
                    resp_users.json()["integrations"],
                )
            )
        )
        == 1
    )
