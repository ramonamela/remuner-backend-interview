from app.integrations.infrastructure.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudPostInputV1,
    IntegrationCrudPostOutputV1,
)


async def integrations_get_v1() -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})


async def integrations__integration_id_get_v1(integration_id: int) -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})


async def integrations_post_v1(
    post_input: IntegrationCrudPostInputV1,
) -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})
    # view_controller = CreateIntegrationViewControllers.v1()
    # return await view_controller(input_team=post_input)


async def integrations_post_v2(
    post_input: IntegrationCrudPostInputV1,
) -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})


async def integrations__integration_id_post_v1(
    post_input: IntegrationCrudPostInputV1,
) -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})


async def integrations__integration_id_delete_v1(
    post_input: IntegrationCrudPostInputV1,
) -> IntegrationCrudPostOutputV1:
    return IntegrationCrudPostOutputV1(**{"id": 1})
