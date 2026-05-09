from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Database Configuration
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "myuser"
    POSTGRES_PASSWORD: str = "mypassword"
    POSTGRES_DB: str = "mydatabase"

    DB_POOL_SIZE: int = 5
    DB_POOL_RECYCLE: int = 3600
    DB_POOL_PRE_PING: bool = True
    DB_MAX_OVERFLOW: int = 10

    @computed_field
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


config: Config = Config()
