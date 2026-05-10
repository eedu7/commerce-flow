from fastapi import APIRouter

from .auth import router as auth_router
from .health import router as health_router
from .user import router as user_router

router = APIRouter()

router.include_router(health_router, prefix="/health", tags=["Health"])
router.include_router(user_router, prefix="/users", tags=["User"])
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
