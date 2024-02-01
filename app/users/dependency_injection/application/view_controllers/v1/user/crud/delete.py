from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.user.v1.crud.delete import DeleteUserViewControllerV1
from app.users.dependency_injection.infrastructure.persistence.user_bo import (
    UserBOPersistenceServices,
)


class DeleteUserViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteUserViewControllerV1,
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
    )
