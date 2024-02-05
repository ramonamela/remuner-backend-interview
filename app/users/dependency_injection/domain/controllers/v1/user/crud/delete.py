from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.users.dependency_injection.persistence.user_bo import (
    UserBOPersistenceServices,
)
from app.users.domain.controllers.v1.user.crud.delete import DeleteUserControllerV1


class DeleteUserControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteUserControllerV1,
        user_bo_persistence_service=UserBOPersistenceServices.remuner,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )
