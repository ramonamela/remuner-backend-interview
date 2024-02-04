from dependency_injector import containers, providers

from app.integrations.dependency_injection.persistence.integration_bo import (
    IntegrationBOPersistenceServices,
)
from app.users.persistence.tortoise.user_bo import UserBOTortoisePersistenceService


class UserBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        UserBOTortoisePersistenceService,
        integration_bo_persistence_service=IntegrationBOPersistenceServices.remuner,
    )

    remuner = tortoise
