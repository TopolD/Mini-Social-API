from fastapi import APIRouter

from app.Public.router import router as public_router
from app.users.router import router as user_router

router = APIRouter()


router.include_router(user_router)
router.include_router(public_router)
