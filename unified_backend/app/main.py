from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import ml_routes, agent_routes, health_routes, analytics_routes

app = FastAPI(title="Urban Air Intelligence Unified Backend", version="1.0.0")

# Mount static directory for serving generated MP3 files
import os
os.makedirs("static/audio", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(ml_routes.router, prefix="/api/v1/ml", tags=["Machine Learning"])
app.include_router(agent_routes.router, prefix="/api/v1/agents", tags=["Agents"])
app.include_router(health_routes.router, prefix="/api/v1/health", tags=["Health Advisory"])
app.include_router(analytics_routes.router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Urban Air Intelligence API"}
