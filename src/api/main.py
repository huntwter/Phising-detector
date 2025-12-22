from fastapi import FastAPI
from src.api.routes import scan_routes, feedback_routes, health_check

app = FastAPI(
    title="Advanced Phishing Detection System API",
    description="Public Gateway for the APDS. Authenticated entry point to the protected Core Logic.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(scan_routes.router)
app.include_router(feedback_routes.router)
app.include_router(health_check.router)
