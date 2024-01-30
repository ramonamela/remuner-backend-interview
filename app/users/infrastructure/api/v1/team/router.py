from fastapi import APIRouter

router = APIRouter()

@router.get("/teams")
async def teams_get():
    return {"message": "Teams get"}

@router.get("/teams/{team_id}")
async def teams__team_id_get():
    return {"message": "Teams id get"}

@router.post("/teams")
async def teams_post():
    return {"message": "Teams post"}

@router.post("/teams/{team_id}")
async def teams__team_id_post():
    return {"message": "Teams id post"}

@router.delete("/teams/{team_id}")
async def teams__team_id_delete():
    return {"message": "Teams id delete"}
