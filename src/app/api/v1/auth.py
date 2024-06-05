from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.app.services.users import UserService


router = APIRouter(prefix='/auth', tags=['auth'])

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# @router.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user = UserService.get(username=form_data.username)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
    # hashed_password = fake_hash_password(form_data.password)
    # if not hashed_password == user.hashed_password:
        # raise HTTPException(status_code=400, detail="Incorrect username or password")

    # return {"access_token": user.username, "token_type": "bearer"}
