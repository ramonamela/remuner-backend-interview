from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello Word from users"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name} from users"}

router.include_router(user_router, prefix="/users", tags=["User"])
router.include_router(team_router, prefix="/teams", tags=["Team"])