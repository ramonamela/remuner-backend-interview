from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.user_bo import (
    UserBOPersistenceServices,
)
from app.users.domain.controllers.v1.user.crud.get import GetUserControllerV1


class GetUserControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetUserControllerV1,
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
