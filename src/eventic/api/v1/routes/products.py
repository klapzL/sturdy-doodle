from typing import List

from fastapi import APIRouter

from src.config.database.session import DBSession

from src.eventic.services.products import ProductService
from src.eventic.schemas.products import ProductSchema, ProductQuerySchema, ProductCreate

router = APIRouter(prefix='/products', tags=['products'])


@router.get('/', response_model=List[ProductSchema])
async def get_products(db: DBSession):
    return await ProductService.get(db)


@router.get('/{product_id}', response_model=ProductQuerySchema)
async def get_product(db: DBSession, product_id: int):
    return await ProductService.get_obj(db, id=product_id)


@router.post('/')
async def create_product(db: DBSession, product: ProductCreate):
    await ProductService.create(db, **product.model_dump())

    return {'message': 'created!'}


@router.put('/{product_id}')
async def update_product(db: DBSession, product_id: int, product: ProductCreate):
    await ProductService.update(db, {'id': product_id}, product.model_dump())

    return {'message': 'updated'}


@router.delete('/{product_id}')
async def remove_product(db: DBSession, product_id: int):
    await ProductService.delete(db, id=product_id)

    return {'message': 'deleted'}
