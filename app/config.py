from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="PSQL_DB_")

    host: str
    port: str
    database: str
    username: str
    password: str


postgres_settings = PostgresSettings()


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")

    host: str
    port: int
    database: int


redis_settings = RedisSettings()


class KeyValueSetings(BaseSettings):

    integrations_counter_key: Optional[str] = "integration_counter_key"
    teams_counter_key: Optional[str] = "teams_counter_key"
    users_counter_key: Optional[str] = "users_counter_key"


key_value_settings = KeyValueSetings()


DATABASE_URL = "postgres://{}:{}@{}:{}/{}".format(
    postgres_settings.username,
    postgres_settings.password,
    postgres_settings.host,
    postgres_settings.port,
    postgres_settings.database,
)

models = ["app.users.models", "app.integrations.models", "aerich.models"]
