from dependency_injector import containers, providers

from app.integrations.infrastructure.persistence.tortoise.integration_bo import (
    IntegrationBOTortoisePersistenceService,
)


class IntegrationBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        IntegrationBOTortoisePersistenceService,
    )

    remuner = tortoise
