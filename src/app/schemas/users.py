from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int

    name: str
    email: str
    phone: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str

    email: EmailStr
    phone: str = None

    password: str
