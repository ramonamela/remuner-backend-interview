from dependency_injector import containers, providers

from app.users.persistence.tortoise import UserBOTortoisePersistenceService


class UserBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        UserBOTortoisePersistenceService,
    )

    remuner = tortoise
