from dependency_injector import containers, providers

from app.users.persistence.tortoise.team_bo import TeamBOTortoisePersistenceService


class TeamBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        TeamBOTortoisePersistenceService,
    )

    remuner = tortoise
