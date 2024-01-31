from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.user.v1.common.input_mapping_service import (
    UserCrudInputMappingServiceV1,
)
from app.users.application.view_controllers.v1.user.v1.crud.create import CreateUserViewControllerV1
from app.users.application.view_controllers.v1.user.v2.common.input_mapping_service import (
    UserCrudInputMappingServiceV2,
)
from app.users.application.view_controllers.v1.user.v2.crud.create import CreateUserViewControllerV2
from app.users.dependency_injection.infrastructure.persistence.user_bo import (
    UserBOPersistenceServices,
)


class CreateUserViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateUserViewControllerV1,
        input_mapping_service=UserCrudInputMappingServiceV1(),
        user_bo_persistence_service=UserBOPersistenceServices.tortoise,
    )

    v2 = providers.Singleton(
        CreateUserViewControllerV2,
        input_mapping_service=UserCrudInputMappingServiceV2(),
        user_bo_persistence_service=UserBOPersistenceServices.tortoise,
    )
