from dependency_injector import containers, providers

from app.integrations.persistence.cached_tortoise.integration_bo import IntegrationBOCachedTortoisePersistenceService
from app.integrations.persistence.tortoise.integration_bo import (
    IntegrationBOTortoisePersistenceService,
)
from remuner_library.persistences.key_value_store.redis.redis import RedisCache


class IntegrationBOPersistenceServices(containers.DeclarativeContainer):

    tortoise = providers.Singleton(
        IntegrationBOTortoisePersistenceService,
    )

    cached_tortoise = providers.Singleton(
        IntegrationBOCachedTortoisePersistenceService, key_value_store=RedisCache()
    )

    remuner = cached_tortoise
