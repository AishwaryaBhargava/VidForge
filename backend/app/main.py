from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.protected import router as protected_router

app = FastAPI(title="VidForge API")

app.include_router(health_router)
app.include_router(protected_router)
