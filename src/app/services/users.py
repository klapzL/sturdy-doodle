from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext

from src.common.service import BaseService

from src.app.models import User


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


class UserService(BaseService):
    model = User

    @classmethod
    def verify_password(form_data_password, hashed_password):
        return pwd_context.verify(form_data_password, hashed_password)

    @classmethod
    def get_hashed_password(user_password):
        return pwd_context.hash(user_password)
