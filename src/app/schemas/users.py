from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int

    name: str
    email: str
    phone: str


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str

    password: str