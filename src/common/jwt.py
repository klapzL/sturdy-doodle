from passlib.context import CryptContext

from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/token')
