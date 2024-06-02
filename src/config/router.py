from fastapi import APIRouter

from src.products.api.v1.endpoints import router as products_router


router = APIRouter(prefix='/api')

router.include_router(products_router)
