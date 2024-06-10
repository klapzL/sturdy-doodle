from fastapi import APIRouter, HTTPException, Depends, status

from src.app.models import User
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


@router.post('/register', response_model=UserSchema)
async def create_user(db: DBSession, user_data: UserCreate = Depends()):

    user = UserService.get_obj(db, username=user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this username already exists'
        )

    password = user_data.password1
    if password != user_data.password2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Passwords do not match'
        )

    new_user = UserService.create(
        db,
        username=user_data.username,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone=user_data.phone,
        hashed_password=UserService.get_hashed_password(password),
    )

    db.add(new_user)
    db.commit()

    return {'message': 'created!'}


@router.get('/me', response_model=UserSchema)
def get_me(db: DBSession):
    user = UserService.get_me(db)

    return user
