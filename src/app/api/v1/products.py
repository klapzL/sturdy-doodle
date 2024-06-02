from fastapi import APIRouter, Depends

from fastapi_pagination import Page

from src.config.database import DBSession

from src.products.services import ProductService
from src.products.schemas import ProductSchema, ProductQuerySchema, ProductCreate

router = APIRouter(prefix='/v1', tags=['products'])


@router.get('/products', response_model=Page[ProductSchema])
def get_products(db: DBSession, product: ProductQuerySchema = Depends()):
    products_filters = product.model_dump(exclude_none=True)
    products = ProductService.get(db, **products_filters)

    return products


@router.get('/products/{product_id}')
def get_product(db: DBSession, product_id: int):
    product = ProductService.get_obj(db, id=product_id)

    return product


@router.post('/products')
def create_product(db: DBSession, product: ProductCreate):
    ProductService.create(db, **product.model_dump())

    return {'details': 'created!'}


@router.delete('/products/{product_id}')
def remove_product(db: DBSession, product_id: int):
    ProductService.delete(db, id=product_id)

    return {'message': 'deleted'}
