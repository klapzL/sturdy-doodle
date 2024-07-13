from fastapi import APIRouter

from src.eventic.api.v1.routes.auth import router as auth_router
from src.eventic.api.v1.routes.users import router as users_router
from src.eventic.api.v1.routes.products import router as products_router

router = APIRouter(prefix='/v1')

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(products_router)
