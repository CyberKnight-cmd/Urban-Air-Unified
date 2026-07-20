from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Dict, Any
from app.services.vulnerability import get_vulnerable_locations
import edge_tts
import os
import uuid

router = APIRouter()

class HealthAdvisoryRequest(BaseModel):
    latitude: float
    longitude: float
    forecast_aqi: int
    primary_pollutant_source: str # e.g., "Industrial", "Biomass"

@router.post("/health-advisory")
async def generate_health_advisory(req: HealthAdvisoryRequest, req_context: Request):
    """
    Generates a localized health advisory and creates real text-to-speech audio files.
    and formatting an LLM prompt.
    """
    # 1. Fetch vulnerable locations
    vulnerable_spots = get_vulnerable_locations(req.latitude, req.longitude)
    
    # 2. Prepare context for the LLM
    vulnerability_summary = {}
    for spot in vulnerable_spots:
        cat = spot["category"]
        vulnerability_summary[cat] = vulnerability_summary.get(cat, 0) + 1
        
    # 3. Generate Advisory (Simulated LLM call for now)
    # In a real implementation, we pass this context to LangGraph/OpenAI
    risk_level = "SEVERE" if req.forecast_aqi > 300 else "HIGH" if req.forecast_aqi > 200 else "MODERATE"
    
    advisory_text = (
        f"URGENT HEALTH ADVISORY: AQI is forecasted to reach {req.forecast_aqi} ({risk_level} risk). "
        f"The primary driver is {req.primary_pollutant_source} pollution. "
    )
    
    if vulnerability_summary:
        advisory_text += f"We have identified high-risk zones in your vicinity, including "
        advisory_text += ", ".join([f"{count} {cat}" for cat, count in vulnerability_summary.items()]) + ". "
        advisory_text += "Please ensure windows are closed and N95 masks are worn outdoors."
    else:
        advisory_text += "Sensitive groups should limit outdoor exertion."

    # 4. Generate Real TTS Audio using edge-tts (British Male Voice)
    audio_id = uuid.uuid4().hex[:8]
    audio_filename_en = f"advisory_{audio_id}_en.mp3"
    audio_path_en = os.path.join("static", "audio", audio_filename_en)
    
    # Save the English audio file
    communicate = edge_tts.Communicate(advisory_text, "en-GB-RyanNeural")
    await communicate.save(audio_path_en)
    
    # Construct the full URL for the frontend
    base_url = str(req_context.base_url).rstrip('/')
    audio_url_en = f"{base_url}/static/audio/{audio_filename_en}"

    # Return Regional Translations & Audio URLs
    return {
        "location": {"latitude": req.latitude, "longitude": req.longitude},
        "forecast_aqi": req.forecast_aqi,
        "vulnerable_locations_found": len(vulnerable_spots),
        "advisory": {
            "english": advisory_text,
            "hindi": "हिंदी अनुवाद यहाँ आएगा। (Hindi translation goes here)",
            "kannada": "ಕನ್ನಡ ಅನುವಾದ ಇಲ್ಲಿ ಬರುತ್ತದೆ. (Kannada translation goes here)"
        },
        "ivr_audio_urls": {
            "english": audio_url_en,
            "hindi": f"{base_url}/static/audio/mock_hindi.mp3" # Can add hindi TTS later!
        }
    }
