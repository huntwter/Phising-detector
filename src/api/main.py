from fastapi import FastAPI
from src.api.v1.routes import analysis
# from src.api.middleware import security

app = FastAPI(
    title="Advanced Phishing Detection System API",
    description="Public Gateway for the APDS. Authenticated entry point to the protected Core Logic.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# app.add_middleware(...)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "apds-gateway"}
