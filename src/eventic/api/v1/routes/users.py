from typing import Annotated

from fastapi import APIRouter, Depends

from src.config.database.session import DBSession
from src.eventic.schemas.auth import UserAuth
from src.eventic.schemas.users import UserCreate
from src.eventic.services.auth import AuthService
from src.eventic.services.users import UserService

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/register/')
async def create_user(db: DBSession, user_data: UserCreate):

    await UserService.check_if_user_exists(
        db, username=user_data.username, email=user_data.email, phone=user_data.phone
    )
    user_data.password = AuthService.get_hashed_password(user_data.password)

    await UserService.create(db, **user_data.model_dump(exclude_none=True))

    return {'message': 'created!'}


@router.get('/me')
def get_me(
    db: DBSession, user: Annotated[UserAuth, Depends(UserService.get_current_user)]
):
    return user
