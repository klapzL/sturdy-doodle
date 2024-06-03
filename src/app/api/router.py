from fastapi import APIRouter

from src.app.api.v1.products import router as products_router


router = APIRouter(prefix='/api')

router.include_router(products_router)
