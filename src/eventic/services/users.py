from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy import select

from src.common.exceptions import BadRequestException
from src.common.jwt import oauth2_scheme
from src.common.service import BaseService
from src.config.database import DBSession
from src.config.settings import settings
from src.eventic.models import User


class UserService(BaseService):
    model = User

    @classmethod
    async def check_if_user_exists(
        cls,
        db: DBSession,
        username: str,
        email: str,
        phone: str | None = None,
    ):

        # Kind bad way, had to rewrite _fetch_records method
        # but it works
        #
        # scalar = await cls._fetch_records(
        #    db,
        #     filters=[
        #         (cls.model.username == username)
        #         | (cls.model.email == email)
        #         | (cls.model.phone == phone),
        #     ],
        # ).first()

        q = select(cls.model).where(
            (cls.model.username == username)
            | (cls.model.email == email)
            | (cls.model.phone == phone)
        )
        result = await db.execute(q)
        user = result.scalars().first()

        if user:
            if user.username == username:
                raise BadRequestException(detail='Username is already taken.')
            if user.email == email:
                raise BadRequestException(detail='Email is already taken.')
            if user.phone == phone:
                raise BadRequestException(detail='Phone number is already taken.')

    @classmethod
    async def get_current_user(
        cls, db: DBSession, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token, settings.TOKEN_SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM]
            )
            username: str = payload.get('sub')
        except jwt.InvalidTokenError:
            raise credentials_exception
        user = await UserService.get_obj(db, username=username)
        return user
