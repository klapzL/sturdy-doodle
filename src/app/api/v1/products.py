from fastapi import APIRouter, Depends

from fastapi_pagination import Page

from src.config.database import DBSession

from src.app.services.products import ProductService
from src.app.schemas.products import ProductSchema, ProductQuerySchema, ProductCreate

router = APIRouter(prefix='/products', tags=['products'])


@router.get('/', response_model=Page[ProductSchema])
def get_products(
    db: DBSession,
    product: ProductQuerySchema = Depends(),
):
    products_filters = product.model_dump(exclude_none=True)
    products = ProductService.get(db, **products_filters)

    return {'items': products}


@router.get('/{product_id}', response_model=ProductQuerySchema)
def get_product(db: DBSession, product_id: int):
    product = ProductService.get_obj(db, id=product_id)

    return product


@router.post('/')
def create_product(db: DBSession, product: ProductCreate):
    ProductService.create(db, **product.model_dump())

    return {'message': 'created!'}


@router.delete('/{product_id}')
def remove_product(db: DBSession, product_id: int):
    ProductService.delete(db, id=product_id)

    return {'message': 'deleted'}
