from dependency_injector import containers, providers

from app.users.api.v1.user.v1.common import (
    UserCrudInputMappingServiceV1,
)
from app.users.api.v1.user.v2.common import (
    UserCrudInputMappingServiceV2,
)
from app.users.application.view_controllers.v1.user.v2.crud.create import CreateUserViewControllerV2
from app.users.dependency_injection.persistence import (
    UserBOPersistenceServices,
)
from app.users.domain.controllers.v1.user.crud import CreateUserViewControllerV1


class CreateUserViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateUserViewControllerV1,
        input_mapping_service=UserCrudInputMappingServiceV1(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )

    v2 = providers.Singleton(
        CreateUserViewControllerV2,
        input_mapping_service=UserCrudInputMappingServiceV2(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
