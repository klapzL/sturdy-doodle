from fastapi import APIRouter

from src.app.api.v1.auth import router as auth_router
from src.app.api.v1.users import router as users_router
from src.app.api.v1.products import router as products_router


router = APIRouter(prefix='/v1')

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(products_router)
