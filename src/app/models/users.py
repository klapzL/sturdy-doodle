from sqlalchemy import Column, String, Integer

from src.common.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)
