import pytest
from async_asgi_testclient import TestClient

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "header, expected_value",
    [
        ("1", 200),
        ("2", 400),
    ],
)
async def test_delete(
    client: TestClient, header, expected_value, integration_bo_factory_db
) -> None:
    integration_bo = await integration_bo_factory_db
    persistence_service = IntegrationBOPersistenceServices.remuner()
    integration_bos = await persistence_service.get_all()
    assert len(integration_bos) == 1
    resp = await client.delete(
        "/v1/integrations/" + str(integration_bo.id),
        headers={"X-API-Version": header},
    )
    assert resp.status_code == expected_value
    team_bos = await persistence_service.get_all()
    if expected_value == 200:
        assert len(team_bos) == 0
