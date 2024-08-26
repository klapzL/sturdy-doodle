from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from src.config.database import DBSession
from src.eventic.schemas.auth import Token
from src.eventic.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', response_model=Token)
async def login(db: DBSession, user: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await AuthService.authenticate_user(db, user.username, user.password)
    access_token = AuthService.create_access_token(user)
    refresh_token = AuthService.create_refresh_token(user)

    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post('/token/refresh', response_model=Token)
async def refresh_token(refresh_token: Annotated[str, Form()]):
    access_token = AuthService.refresh_token(refresh_token)
    return Token(access_token=access_token, refresh_token=refresh_token)
