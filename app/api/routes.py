from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API root OK"}

@router.get("/api")
async def root():
    return {"message": "Hello from FastAPI Skeleton"}

@router.get("/api/")
async def api_with_slash():
    return {"message": "Hello from FastAPI Skeleton"}
