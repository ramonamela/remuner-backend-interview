from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.user.v1.common.input_mapping_service import (
    UserCrudInputMappingServiceV1,
)
from app.users.application.view_controllers.v1.user.v1.crud.update import UpdateUserViewControllerV1
from app.users.application.view_controllers.v1.user.v2.common.input_mapping_service import (
    UserCrudInputMappingServiceV2,
)
from app.users.application.view_controllers.v1.user.v2.crud.update import UpdateUserViewControllerV2
from app.users.dependency_injection.infrastructure.persistence.user_bo import (
    UserBOPersistenceServices,
)


class UpdateUserViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        UpdateUserViewControllerV1,
        input_mapping_service=UserCrudInputMappingServiceV1(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )

    v2 = providers.Singleton(
        UpdateUserViewControllerV2,
        input_mapping_service=UserCrudInputMappingServiceV2(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
