from dependency_injector import containers, providers

from app.users.persistence.tortoise.user_bo import UserBOTortoisePersistenceService


class UserBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        UserBOTortoisePersistenceService,
    )

    remuner = tortoise
