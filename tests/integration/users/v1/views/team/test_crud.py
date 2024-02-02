import pytest
from async_asgi_testclient import TestClient

from app.users.api.v1.team.v1.crud.swagger_examples import crud_post_input_v1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, key, expected_value", [("1", "name", 200), ("2", "name", 400), ("1", "random", 422)]
)
async def test_create(client: TestClient, header, key, expected_value) -> None:
    resp = await client.post(
        "/v1/teams",
        json={
            key: "test_team" + str(header),
        },
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value


@pytest.mark.asyncio
async def test_create_swagger(client: TestClient) -> None:
    resp = await client.post("/v1/teams", json=crud_post_input_v1, headers={"X-API-Version": "1"})
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_create_repeated(client: TestClient) -> None:
    resp = await client.post(
        "/v1/teams",
        json={
            "name": "test_team1",
        },
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 200

    resp = await client.post(
        "/v1/teams",
        json={
            "name": "test_team1",
        },
        headers={"X-API-Version": "1"},
    )
    assert resp.status_code == 409
