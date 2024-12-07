from datetime import datetime, timedelta, timezone
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database.session import get_db_session
from src.config.settings import pwd_context, settings
from src.eventic.constants.auth import (
    ACCESS_TOKEN_TYPE,
    JWT_EXPIRATION_KEY,
    JWT_JTI_KEY,
    JWT_NOT_BEFORE_KEY,
    JWT_SUBJECT_KEY,
    JWT_TYPE_KEY,
    REFRESH_TOKEN_TYPE,
)
from src.eventic.models.users import User
from src.eventic.services.users import UserService


class AuthService:
    auth_model = User

    @classmethod
    def get_hashed_password(cls, user_password):
        return pwd_context.hash(user_password)

    @classmethod
    def verify_password(cls, password, hashed_password):
        return pwd_context.verify(password, hashed_password)

    @staticmethod
    def create_token(username: str, expires_delta: timedelta, token_type: str):
        now = datetime.now(timezone.utc)

        data = {
            JWT_SUBJECT_KEY: username,
            JWT_NOT_BEFORE_KEY: now,
            JWT_EXPIRATION_KEY: now + expires_delta,
            JWT_JTI_KEY: str(uuid4()),
            JWT_TYPE_KEY: token_type,
        }

        encoded_jwt = jwt.encode(
            payload=data,
            key=settings.TOKEN_SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM,
        )

        return encoded_jwt

    @classmethod
    def create_access_token(cls, username):
        expire_delta = timedelta(minutes=settings.TOKEN_ACCESS_EXPIRE_MINUTES)

        return cls.create_token(username, expire_delta, ACCESS_TOKEN_TYPE)

    @classmethod
    def create_refresh_token(cls, username):
        expire_delta = timedelta(minutes=settings.TOKEN_REFRESH_EXPIRE_MINUTES)

        return cls.create_token(username, expire_delta, REFRESH_TOKEN_TYPE)

    @classmethod
    def refresh_token(cls, refresh_token):
        try:
            payload = jwt.decode(
                refresh_token,
                settings.TOKEN_SECRET_KEY,
                algorithms=[settings.TOKEN_ALGORITHM],
            )
            username = payload.get(JWT_SUBJECT_KEY)
            UserService
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        return cls.create_access_token(username)

    @classmethod
    async def authenticate_user(
        cls,
        db: Annotated[AsyncSession, Depends(get_db_session)],
        username: str,
        password: str,
    ):
        user = await UserService.get_obj(
            db,
            [
                (cls.auth_model.username == username)
                | (cls.auth_model.email == username)
            ],
        )

        if not cls.verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        return user.username
