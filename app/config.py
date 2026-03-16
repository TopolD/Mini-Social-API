from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DATABASE_URL: str
    TEST_DATABASE_URL: str

    SECRET_KEY_ACCESS: str
    SECRET_KEY_REFRESH: str
    ALGORITHM: str

    ACCESS_TIME_TOKEN: int
    REFRESH_TOKEN_EXPIRATION: int

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
