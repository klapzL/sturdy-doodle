from pydantic import BaseModel, ConfigDict

from src.products.enums import ProductType


class ProductSchema(BaseModel):
    id: int

    name: str
    price: float
    type: ProductType

    model_config = ConfigDict(from_attributes=True)


class ProductQuerySchema(BaseModel):
    name: str | None = None
    price: float | None = None
    type: ProductType | None = None


class ProductCreate(BaseModel):
    name: str
    price: float
    type: ProductType
