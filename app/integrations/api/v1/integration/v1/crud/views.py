from typing import List

from fastapi import HTTPException

from app.integrations.api.v1.integration.v1.common.output_mapping_service import (
    IntegrationOutputMappingServiceV1,
)
from app.integrations.api.v1.integration.v1.common.view_models import (
    IntegrationIdOutputV1,
    IntegrationOutputV1,
)
from app.integrations.api.v1.integration.v1.crud.input_mapping_service import (
    IntegrationCrudInputMappingServiceV1,
)
from app.integrations.api.v1.integration.v1.crud.view_models import (
    IntegrationCrudInputV1,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.create import (
    CreateIntegrationControllers,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.delete import (
    DeleteIntegrationControllers,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.get import (
    GetIntegrationControllers,
)
from app.integrations.dependency_injection.application.view_controllers.v1.integration.crud.update import (
    UpdateIntegrationControllers,
)
from app.integrations.domain.persistence.exceptions.integration_bo import (
    IntegrationNotFoundException,
    RepeatedIntegrationNameException,
)


async def integrations_get_v1() -> List[IntegrationOutputV1]:
    view_controller = GetIntegrationControllers.v1()
    output_mapping_service = IntegrationOutputMappingServiceV1()
    return [output_mapping_service(integration_bo) for integration_bo in await view_controller()]


async def integrations__integration_id_get_v1(integration_id: int) -> IntegrationOutputV1:
    view_controller = GetIntegrationControllers.v1()
    output_mapping_service = IntegrationOutputMappingServiceV1()
    return await output_mapping_service(view_controller(integration_id=integration_id))


async def integrations_post_v1(
    post_input: IntegrationCrudInputV1,
) -> IntegrationIdOutputV1:
    view_controller = CreateIntegrationControllers.v1()
    input_mapping_service = IntegrationCrudInputMappingServiceV1()
    try:
        return IntegrationIdOutputV1(
            id=await view_controller(integration_bo=input_mapping_service(post_input))
        )
    except RepeatedIntegrationNameException:
        raise HTTPException(
            status_code=409, detail="Integration name already exists in the database"
        )


async def integrations__integration_id_post_v1(
    integration_id: int, post_input: IntegrationCrudInputV1
) -> IntegrationIdOutputV1:
    view_controller = UpdateIntegrationControllers.v1()
    input_mapping_service = IntegrationCrudInputMappingServiceV1()

    integration_bo = input_mapping_service(input_integration=post_input)
    try:
        return IntegrationIdOutputV1(
            id=await view_controller(integration_id=integration_id, integration_bo=integration_bo)
        )
    except IntegrationNotFoundException:
        raise HTTPException(status_code=404, detail="Integration not found")


async def integrations__integration_id_delete_v1(
    integration_id: int,
):
    view_controller = DeleteIntegrationControllers.v1()
    try:
        await view_controller(integration_id=integration_id)
        return {}
    except IntegrationNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")
