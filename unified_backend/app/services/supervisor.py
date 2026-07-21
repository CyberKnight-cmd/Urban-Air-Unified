from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

from app.services.ml_inference import run_inference
from app.services.nearby_sources import get_nearby_sources
from app.services.scoring import rank_pollution_sources
from app.services.recommendation import generate_recommendations
from app.services.vulnerability import get_vulnerable_locations

@tool
def get_aqi_forecast_and_attribution(latitude: float, longitude: float):
    """Fetches the 48-hour AQI forecast and pollution source attribution percentages for a given coordinate."""
    return run_inference(latitude, longitude)

@tool
def get_enforcement_plan(latitude: float, longitude: float, current_aqi: int, forecast_aqi: int, traffic_pct: float, industrial_pct: float, biomass_pct: float):
    """Generates an enforcement plan prioritizing local polluters (industries, construction, etc.) based on ML source attribution."""
    sources = get_nearby_sources(latitude, longitude)
    ranked = rank_pollution_sources(sources, current_aqi, forecast_aqi, traffic_pct, industrial_pct, biomass_pct)
    return generate_recommendations(ranked, current_aqi, forecast_aqi)

@tool
def get_health_advisory(latitude: float, longitude: float, forecast_aqi: int, primary_pollutant: str):
    """Generates a health advisory by mapping vulnerable populations (hospitals, schools, nursing homes) around the hotspot."""
    spots = get_vulnerable_locations(latitude, longitude)
    
    summary = {}
    for s in spots:
        summary[s["category"]] = summary.get(s["category"], 0) + 1
        
    return {
        "vulnerable_locations_count": len(spots),
        "details": summary,
        "advice": f"AQI is {forecast_aqi} due to {primary_pollutant}. Protect sensitive groups in these facilities."
    }

tools = [get_aqi_forecast_and_attribution, get_enforcement_plan, get_health_advisory]

def get_supervisor_app():
    """
    Initializes the LangGraph ReAct agent that orchestrates the workflow.
    Requires GEMINI_API_KEY in the environment.
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    
    system_prompt = (
        "You are the Urban Air Intelligence Supervisor, an AI orchestrator for city officials. "
        "You have access to 3 tools: AQI forecasting/attribution, Enforcement planning, and Health advisory mapping. "
        "Answer the user's queries by calling the appropriate tools. If they don't provide coordinates, ask for them."
    )
    
    agent_executor = create_react_agent(model, tools, prompt=system_prompt)
    return agent_executor
