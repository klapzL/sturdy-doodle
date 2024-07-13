from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    DEBUG: bool = True

    TOKEN_SECRET_KEY: str = 'secret'
    TOKEN_ALGORITHM: str = 'HS256'
    TOKEN_ACCESS_EXPIRE_MINUTES: int = 60 * 24 * 7
    TOKEN_REFRESH_EXPIRE_MINUTES: int = 60 * 24 * 7

    SQLALCHEMY_DATABASE_URI: str = 'sqlite+aiosqlite:///sqlite.db'
    ALEMBIC_DATABASE_URI: str = 'sqlite:///sqlite.db'

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str


settings = Settings()
