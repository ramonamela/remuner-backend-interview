from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.user_bo import UserBOPersistenceServices
from app.users.domain.controllers.v1.user.crud.update import UpdateUserControllerV1


class UpdateUserControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        UpdateUserControllerV1,
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
