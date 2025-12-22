from fastapi import APIRouter

router = APIRouter()

@router.post("/scan")
async def scan_url():
    """
    Initiate a phishing scan.
    This route acts as a facade, delegating the actual work to the `src.core`
    via the Application Layer or offloading to `src.workers`.
    """
    pass
