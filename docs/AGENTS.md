# 🤖 AI Agents & Geospatial Enforcement Logic

The backend uses a blend of Deterministic Geospatial Queries (OSMnx) and Generative AI (LangGraph) to turn raw pollution data into actionable municipal enforcement plans.

## 1. The OSMnx Overpass Query Engine
We use `osmnx` (a Python wrapper for the OpenStreetMap Overpass API) to map physical infrastructure.

### Health Advisory Vulnerability Targeting (`vulnerability.py`)
When a Health Advisory is generated, the backend draws a 2km bounding box around the target coordinates and queries OpenStreetMap for the following tags:
- `amenity: school`
- `amenity: hospital`
- `amenity: clinic`
- `amenity: social_facility`
The length of the returned GeoDataFrame represents the exact number of vulnerable buildings in the blast radius of the pollution plume. This context is injected into the LLM prompt.

### Enforcement Infrastructure Targeting (`nearby_sources.py`)
If the NMF model attributes pollution primarily to **Industrial** sources (e.g., >50%), the backend dynamically alters its OSM query to search for:
- `landuse: industrial`
- `man_made: works`
- `power: plant`
If the primary source is **Traffic**, it queries for:
- `highway: trunk`
- `highway: primary`

## 2. The Enforcement Scoring Algorithm (`scoring.py`)
Once OSMnx returns a list of 50+ factories or highways in the city, the backend must rank them so inspectors know where to go first.
1. **Haversine Distance:** We calculate the exact spherical earth distance (in km) from the epicenter to the factory.
2. **Relevance Multiplier:** A factory gets a higher baseline score than a small warehouse.
3. **Decay Function:** The score decays exponentially as distance increases (`score = base_score / (distance_km + 1)`).
4. The JSON response returns the top 5 targets sorted by this score.

## 3. The LangGraph ReAct Supervisor (`supervisor.py`)
To make the entire system autonomous, we deployed a **ReAct** (Reasoning + Acting) Agent using `langgraph` and `langchain_openai`.

- **Tools:** The agent is bound to three Python functions: `get_aqi_forecast_and_attribution()`, `get_enforcement_plan()`, and `get_health_advisory()`.
- **System Prompt:** The agent is instructed that it is the "Chief Environmental Officer".
- **Workflow:** When a user sends a chat message like *"I am the mayor of Bangalore. What is the situation today and what should I do?"*
  1. The LLM enters a Reasoning loop. It realizes it needs data for Bangalore.
  2. It autonomously calls `get_aqi_forecast_and_attribution` with Bangalore's coordinates.
  3. It reads the JSON response (e.g., AQI is 269, Industrial is 60%).
  4. It reasons it needs to plan enforcement. It autonomously calls `get_enforcement_plan`.
  5. It synthesizes all this data into a comprehensive, natural language report for the user, completely automatically.
