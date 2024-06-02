from sqlalchemy import Column, String, Integer, Enum, Float

from src.common.models import BaseModel
from src.app.enums.products import ProductType


class Product(BaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    price = Column(Float)
    type = Column(Enum(ProductType))
