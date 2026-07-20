from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ml_inference import run_inference

router = APIRouter()

class PredictionRequest(BaseModel):
    latitude: float
    longitude: float

@router.post("/predict")
def predict_aqi(req: PredictionRequest):
    """
    Core ML endpoint that runs the source attribution and forecasting models
    for a given coordinate.
    """
    result = run_inference(req.latitude, req.longitude)
    return result
