from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nearby_sources import get_nearby_sources
from app.services.scoring import rank_pollution_sources
from app.services.recommendation import generate_recommendations
from app.services.supervisor import get_supervisor_app

router = APIRouter()

class EnforcementRequest(BaseModel):
    latitude: float
    longitude: float
    current_aqi: int
    forecast_aqi: int
    traffic_pct: float = 0.0
    industrial_pct: float = 0.0
    biomass_pct: float = 0.0

@router.post("/enforcement")
def generate_enforcement(req: EnforcementRequest):
    """
    Generates enforcement recommendations by correlating ML predictions 
    with OpenStreetMap data (Phase 3.1 of the Master Plan).
    """
    sources = get_nearby_sources(req.latitude, req.longitude)
    
    ranked_sources = rank_pollution_sources(
        sources, 
        req.current_aqi, 
        req.forecast_aqi,
        req.traffic_pct,
        req.industrial_pct,
        req.biomass_pct
    )
    
    report = generate_recommendations(ranked_sources, req.current_aqi, req.forecast_aqi)
    
    return report

class ChatRequest(BaseModel):
    message: str
    latitude: float = 28.6304
    longitude: float = 77.2177

@router.post("/chat")
def chat_with_supervisor(req: ChatRequest):
    """
    LangGraph Multi-Agent Supervisor Endpoint.
    Converses with the AI to fetch forecasts, health advisories, or enforcement plans.
    """
    try:
        app_supervisor = get_supervisor_app()
        
        # Inject the coordinates into the user's message context
        context_msg = f"User location context: lat={req.latitude}, lon={req.longitude}. Query: {req.message}"
        inputs = {"messages": [("user", context_msg)]}
        
        result = app_supervisor.invoke(inputs)
        content = result["messages"][-1].content
        if isinstance(content, list) and len(content) > 0 and "text" in content[0]:
            reply_text = content[0]["text"]
        else:
            reply_text = str(content)
            
        return {"reply": reply_text}
    except Exception as e:
        return {"error": str(e), "note": "Ensure GEMINI_API_KEY is set in your .env file to use the LangGraph supervisor."}
