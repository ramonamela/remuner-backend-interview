from fastapi import HTTPException

from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.create import (
    CreateIntegrationViewControllers,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.delete import (
    DeleteIntegrationViewControllers,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.get import (
    GetIntegrationViewControllers,
)
from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudIdOutputV1,
    IntegrationCrudInputV1,
)
from app.integrations.infrastructure.persistence.exceptions.integration_bo import (
    IntegrationNotFoundException, RepeatedIntegrationNameException,
)


async def integrations_get_v1() -> IntegrationCrudIdOutputV1:
    view_controller = GetIntegrationViewControllers.v1()
    return await view_controller()


async def integrations__integration_id_get_v1(integration_id: int) -> IntegrationCrudIdOutputV1:
    view_controller = GetIntegrationViewControllers.v1()
    return await view_controller(integration_id=integration_id)


async def integrations_post_v1(
    post_input: IntegrationCrudInputV1,
) -> IntegrationCrudIdOutputV1:
    view_controller = CreateIntegrationViewControllers.v1()
    try:
        return await view_controller(input_integration=post_input)
    except RepeatedIntegrationNameException:
        raise HTTPException(status_code=409, detail="Integration name already exists in the database")


async def integrations__integration_id_post_v1(
    integration_id: int, post_input: IntegrationCrudInputV1
) -> IntegrationCrudIdOutputV1:
    return IntegrationCrudIdOutputV1(**{"id": 1})


async def integrations__integration_id_delete_v1(
    integration_id: int,
) -> IntegrationCrudIdOutputV1:
    view_controller = DeleteIntegrationViewControllers.v1()
    try:
        return await view_controller(integration_id=integration_id)
    except IntegrationNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")
