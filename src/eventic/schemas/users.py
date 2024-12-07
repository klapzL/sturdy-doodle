from pydantic import BaseModel, EmailStr
from pydantic.config import ConfigDict


class UserSchema(BaseModel):
    id: int

    full_name: str
    email: str
    phone: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str

    username: str
    email: EmailStr
    phone: str | None = None

    password: str

    model_config = ConfigDict(from_attributes=True)
