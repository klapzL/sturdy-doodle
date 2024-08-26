from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException
from sqlalchemy import or_

from src.common.jwt import pwd_context
from src.config.database import DBSession
from src.config.settings import settings
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

    def create_token(self, username: str, expires_delta: timedelta):
        exp = datetime.now(timezone.utc) + expires_delta

        data = {
            'sub': username,
            'exp': exp,
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

        return cls.create_token(cls, username, expires_delta=expire_delta)

    @classmethod
    def create_refresh_token(cls, username):
        expire_delta = timedelta(minutes=settings.TOKEN_REFRESH_EXPIRE_MINUTES)

        return cls.create_token(cls, username, expires_delta=expire_delta)

    @classmethod
    def refresh_token(cls, refresh_token):
        try:
            payload = jwt.decode(
                refresh_token,
                settings.TOKEN_SECRET_KEY,
                algorithms=[settings.TOKEN_ALGORITHM],
            )
            username = payload.get('sub')
            UserService
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

        return cls.create_access_token(username)

    @classmethod
    async def authenticate_user(cls, db: DBSession, username: str, password: str):
        user = await UserService.get(
            db,
            or_(
                (cls.auth_model.username == username),
                (cls.auth_model.email == username),
            ),
        )

        if not cls.verify_password(password, user.password):
            raise HTTPException(status_code=401, detail='Incorrect password')

        return user.username
