from dependency_injector import containers, providers

from app.users.api.v1.user.v1.common import (
    UserCrudOutputMappingServiceV1,
)
from app.users.api.v1.user.v2.common import (
    UserCrudOutputMappingServiceV2,
)
from app.users.application.view_controllers.v1.user.v2.crud.get import GetUserViewControllerV2
from app.users.dependency_injection.persistence.user_bo import (
    UserBOPersistenceServices,
)
from app.users.domain.controllers.v1.user.crud import GetUserViewControllerV1


class GetUserViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetUserViewControllerV1,
        output_mapping_service=UserCrudOutputMappingServiceV1(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )

    v2 = providers.Singleton(
        GetUserViewControllerV2,
        output_mapping_service=UserCrudOutputMappingServiceV2(),
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
