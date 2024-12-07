from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status

from src.common.exceptions import BadRequestException
from src.common.service import BaseService
from src.config.database import DBSession
from src.config.settings import oauth2_scheme, settings
from src.eventic.constants.auth import JWT_SUBJECT_KEY
from src.eventic.models import User


class UserService(BaseService[User]):
    model = User

    @classmethod
    async def check_if_user_exists(
        cls,
        db: DBSession,
        username: str,
        email: str,
        phone: str | None = None,
    ) -> None:
        user = await cls.get_obj(
            db,
            [
                (cls.model.username == username)
                | (cls.model.email == email)
                | (cls.model.phone == phone),
            ],
        )

        if user:
            if user.username == username:
                raise BadRequestException(detail="Username is already taken.")
            if user.email == email:
                raise BadRequestException(detail="Email is already taken.")
            if user.phone == phone:
                raise BadRequestException(detail="Phone number is already taken.")

    @classmethod
    async def get_current_user(
        cls, db: DBSession, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
        try:
            payload = jwt.decode(
                token, settings.TOKEN_SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM]
            )
            username: str = payload.get(JWT_SUBJECT_KEY)
        except jwt.InvalidTokenError:
            raise credentials_exception
        user = await cls.get_obj(db, [cls.model.username == username])
        return user
