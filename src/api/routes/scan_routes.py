from fastapi import APIRouter, Depends
from src.api.dependencies.authentication import verify_api_key

router = APIRouter(prefix="/scan", tags=["Scanning"])

@router.post("/", dependencies=[Depends(verify_api_key)])
async def submit_scan(url: str):
    return {"message": "Scan initiated", "url": url}
