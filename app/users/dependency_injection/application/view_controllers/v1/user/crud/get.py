from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.user.v1.common.output_mapping_service import (
    UserCrudOutputMappingServiceV1,
)
from app.users.application.view_controllers.v1.user.v1.crud.get import GetUserViewControllerV1
from app.users.application.view_controllers.v1.user.v2.common.output_mapping_service import (
    UserCrudOutputMappingServiceV2,
)
from app.users.application.view_controllers.v1.user.v2.crud.get import GetUserViewControllerV2
from app.users.dependency_injection.infrastructure.persistence.user_bo import (
    UserBOPersistenceServices,
)


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
