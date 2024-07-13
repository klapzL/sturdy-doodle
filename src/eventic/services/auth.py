import jwt

from datetime import datetime, timedelta, timezone

from fastapi import HTTPException

from sqlalchemy import or_

from src.config.database import DBSession
from src.config.settings import settings

from src.common.jwt import pwd_context

from src.eventic.models.users import User
from src.eventic.services.users import UserService

class AuthService:
    auth_model = User

    @classmethod
    def get_hashed_password(cls, user_password):
        return pwd_context.hash(user_password)

    @classmethod
    def verify_password(cls, form_data_password, hashed_password):
        return pwd_context.verify(form_data_password, hashed_password)

    @classmethod
    def create_access_token(cls, user):
        data = {'sub': user.username}
        to_encode = data.copy()

        expires_delta = timedelta(minutes=settings.TOKEN_ACCESS_EXPIRE_MINUTES)
        exp = datetime.now(timezone.utc) + expires_delta

        to_encode.update({'exp': exp})

        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=settings.TOKEN_SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM,
        )

        return encoded_jwt

    @classmethod
    async def authenticate_user(cls, db: DBSession, username: str, password: str):
        user = await UserService.get_all(db, or_(
            (cls.auth_model.username == username),
            (cls.auth_model.email == username),
        ))

        if not cls.verify_password(password, user.password):
            raise HTTPException(
                status_code=401, detail='Incorrect password'
            )

        return user
