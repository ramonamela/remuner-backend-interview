from fastapi import APIRouter

from app.users.api.v1.team.router import router as team_router
from app.users.api.v1.user.router import router as user_router

router = APIRouter()

router.include_router(team_router, prefix="", tags=["UsersApp"])
router.include_router(user_router, prefix="", tags=["UsersApp"])
