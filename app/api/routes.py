from fastapi import APIRouter

router = APIRouter()

@router.get("/api")
async def root():
    return {"message": "Hello from FastAPI Skeleton"}
