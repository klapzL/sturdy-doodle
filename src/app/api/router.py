from fastapi import APIRouter

from src.app.api.v1.router import router as api_v1_router


router = APIRouter(prefix='/api')

router.include_router(api_v1_router)
