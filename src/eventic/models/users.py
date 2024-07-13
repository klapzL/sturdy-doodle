from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import column_property

from src.common.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)
    full_name = column_property(f'{first_name} {last_name}')

    username = Column(String, unique=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True, nullable=True)
    password = Column(String)
