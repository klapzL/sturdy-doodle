from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True

    TOKEN_SECRET_KEY: str = "secret"
    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_ACCESS_EXPIRE_MINUTES: int = 60 * 24 * 7
    TOKEN_REFRESH_EXPIRE_MINUTES: int = 60 * 24 * 7

    SQLALCHEMY_DATABASE_URI: str = "sqlite+aiosqlite:///sqlite.db"
    ALEMBIC_DATABASE_URI: str = "sqlite:///sqlite.db"

    RMQ_USER: str = Field(validation_alias="RABBITMQ_DEFAULT_USER")
    RMQ_PASSWORD: str = Field(validation_alias="RABBITMQ_DEFAULT_PASS")
    RMQ_HOST: str = Field(validation_alias="RABBITMQ_HOST_NAME")
    RMQ_PORT: int = Field(validation_alias="RABBITMQ_PORT")
    RMQ_QUEUE: str = Field(validation_alias="RABBITMQ_QUEUE")

    @property
    def RMQ_URL(self):
        return f"amqp://{self.RMQ_USER}:{self.RMQ_PASSWORD}@{self.RMQ_HOST}:{self.RMQ_PORT}/"


settings = Settings()  # type: ignore


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")
