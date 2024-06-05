from fastapi import APIRouter

from src.config.database import DBSession
from src.app.services.users import UserService
from src.app.schemas.users import UserSchema, UserCreate

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/register')
def register(db: DBSession, user: UserCreate):
    UserService.create(db, **user.model_dump())

    return {'message': 'created'}


def get_current_user(db: DBSession):
    user = UserService.get_me(db)

    return user


@router.get('/me', response_model=UserSchema)
def get_me(db: DBSession):
    user = UserService.get_me(db)

    return user
