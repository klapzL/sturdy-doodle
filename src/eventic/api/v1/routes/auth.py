from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.config.database import DBSession

from src.eventic.services.auth import AuthService
from src.eventic.schemas.auth import Token


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', response_model=Token)
async def login(db: DBSession, user: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await AuthService.authenticate_user(db, user.username, user.password)
    access_token = AuthService.create_access_token(user)

    return {'access_token': access_token, 'token_type': 'bearer'}
