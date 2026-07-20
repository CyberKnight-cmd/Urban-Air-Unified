# 🌐 Urban Air Intelligence: Complete API Reference

Welcome to the definitive API documentation for the **Urban Air Intelligence Unified Backend**. This document provides an exhaustive, 360-degree view of every REST endpoint exposed by the FastAPI orchestrator. It is designed to be fully comprehensible for frontend developers, future AI agents, and DevOps engineers. 

Each endpoint breakdown includes the underlying business logic, exact request payload schemas, HTTP status codes, error handling mechanisms, and the complete structure of the JSON responses.

---

## 1. Machine Learning & Geospatial Inference
### `POST /api/v1/ml/predict`

**Overview:** 
This is the core predictive engine of the architecture. Unlike traditional ML endpoints that require pre-compiled CSVs, this route acts as a real-time orchestrator. When called, it dynamically reaches out to the Open-Meteo external API to fetch exactly 168 hours (7 days) of trailing historical weather and pollution data for the specific GPS coordinate provided. It engineers time-series lag features, patches missing sensor data using a `MissForest` imputer (backed by LightGBM), and runs the data through pre-trained XGBoost and Non-Negative Matrix Factorization (NMF) `.pkl` models. Finally, it uses `geopy` to calculate a live wind-dispersion pollution plume.

**cURL Example:**
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/ml/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latitude": 28.6304,
  "longitude": 77.2177
}'
```

**Request Payload Schema:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `latitude` | `float` | Yes | The GPS latitude of the target prediction zone. |
| `longitude`| `float` | Yes | The GPS longitude of the target prediction zone. |

**Success Response (200 OK):**
```json
{
  "station": "Live_OpenMeteo_Node",
  "timestamp": "2026-07-24T23:00:00.000000",
  "attribution": {
    "traffic_pct": 0.9713,
    "industrial_pct": 0.0286,
    "biomass_pct": 0.0,
    "solvent_voc_pct": 0.0,
    "confidence": 0.0
  },
  "forecast_pm25": {
    "1h": 22.73,
    "24h": 33.51,
    "48h": 58.06
  },
  "dispersion_plume": {
    "type": "Feature",
    "properties": {
      "forecast_aqi": 33.52,
      "wind_speed_ms": 10.5,
      "wind_direction_deg": 93.0,
      "risk_level": "LOW"
    },
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [77.2177, 28.6304],
          [77.0077, 28.5908],
          [76.9817, 28.6411],
          [77.0133, 28.6887],
          [77.2177, 28.6304]
        ]
      ]
    }
  },
  "location": {
    "latitude": 28.6304,
    "longitude": 77.2177
  }
}
```

**Response Field Breakdown:**
- **`station`**: Will read `"Live_OpenMeteo_Node"` if the live data ingestion succeeded, or `"Fallback_Mock_Node"` if the Open-Meteo API failed or the ML pipeline crashed.
- **`attribution`**: NMF matrix outputs representing the percentage of pollution caused by each sector. Must sum to ~1.0. 
- **`forecast_pm25`**: Output from the XGBoost time-series regressor for 1-hour, 24-hour, and 48-hour horizons.
- **`dispersion_plume`**: A strictly formatted `GeoJSON` Feature (Polygon). Calculated mathematically using the live wind speed (`wind_speed_ms`) and wind direction (`wind_direction_deg`) to model a directional pollution plume blowing downwind from the origin coordinate.

**Error Handling:**
If Open-Meteo rate limits the server, or the ML pipeline throws a `ValueError`, this endpoint will gracefully catch the exception and return a simulated fallback object. It will never return a 500 Internal Server Error unless the server itself runs out of memory.

---

## 2. Health Advisory & Audio Generation
### `POST /api/v1/health/health-advisory`

**Overview:** 
This route powers the "Citizen Health Risk Advisory System". It uses `OSMnx` to perform a 2km bounding box query against the live OpenStreetMap database to map physical vulnerable locations (schools, hospitals, clinics). It synthesizes this vulnerability data with the forecasted AQI into a natural language advisory. Finally, it uses `edge-tts` (Microsoft Azure Neural Voices) to generate a professional, British-accented `.mp3` audio file of the advisory asynchronously, writing it to the server's disk and returning the public URL.

**cURL Example:**
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/health/health-advisory' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latitude": 12.9716,
  "longitude": 77.5946,
  "forecast_aqi": 269,
  "primary_pollutant_source": "Industrial"
}'
```

**Request Payload Schema:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `latitude` | `float` | Yes | Target GPS coordinate. |
| `longitude`| `float` | Yes | Target GPS coordinate. |
| `forecast_aqi` | `int` | Yes | The AQI forecast (usually extracted from the `/predict` route). |
| `primary_pollutant_source` | `str` | Yes | Extracted from the highest NMF attribution percentage. |

**Success Response (200 OK):**
```json
{
  "location": {
    "latitude": 12.9716,
    "longitude": 77.5946
  },
  "forecast_aqi": 269,
  "vulnerable_locations_found": 150,
  "advisory": {
    "english": "URGENT HEALTH ADVISORY: AQI is forecasted to reach 269 (HIGH risk)...",
    "hindi": "हिंदी अनुवाद यहाँ आएगा। (Hindi translation goes here)",
    "kannada": "ಕನ್ನಡ ಅನುವಾದ ಇಲ್ಲಿ ಬರುತ್ತದೆ. (Kannada translation goes here)"
  },
  "ivr_audio_urls": {
    "english": "http://localhost:8000/static/audio/advisory_354cac69_en.mp3",
    "hindi": "http://localhost:8000/static/audio/mock_hindi.mp3"
  }
}
```

**Response Field Breakdown:**
- **`vulnerable_locations_found`**: The raw integer count of matching OSM Nodes (amenities) in the 2km radius.
- **`advisory.english`**: The synthesized natural language warning.
- **`ivr_audio_urls.english`**: A static, playable `.mp3` URI generated instantly by `edge-tts`. Hosted directly by FastAPI's `StaticFiles` mount.

---

## 3. Geospatial Enforcement AI
### `POST /api/v1/agents/enforcement`

**Overview:** 
This endpoint translates machine learning data into actionable municipal enforcement. It takes the NMF attribution percentages and dynamically alters its `OSMnx` queries based on the primary polluter. If Traffic is high, it queries for `highway: primary`. If Industry is high, it queries for `landuse: industrial`. It calculates the Haversine distance from the epicenter to these infrastructure nodes and runs them through a custom scoring algorithm (`app/services/scoring.py`), returning the top 5 targets for inspection.

**cURL Example:**
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/agents/enforcement' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "latitude": 12.9716,
  "longitude": 77.5946,
  "current_aqi": 85,
  "forecast_aqi": 269,
  "traffic_pct": 0.4,
  "industrial_pct": 0.5,
  "biomass_pct": 0.1
}'
```

**Success Response (200 OK):**
```json
{
  "hotspot": {
    "current_aqi": 85,
    "forecast_aqi": 269,
    "risk_level": "Low"
  },
  "top_sources": [
    {
      "name": "Cubbon Park 4MLD Sewage Treatment Planet",
      "category": "Industry",
      "distance_km": 0.37,
      "latitude": 12.970684,
      "longitude": 77.591355,
      "score": 100
    }
  ],
  "recommendations": [
    "Inspect industrial facility 'Cubbon Park 4MLD Sewage Treatment Planet' for emission compliance."
  ]
}
```

---

## 4. LangGraph Supervisor LLM
### `POST /api/v1/agents/chat`

**Overview:** 
A ReAct agent powered by LangGraph and OpenAI (`gpt-4o-mini`). The agent has been equipped with python tools that call the other 3 routes under the hood. It allows users to issue natural language commands (e.g., *"What is the forecast for Mumbai and what enforcement should we take?"*) and receive synthesized, autonomous answers. 

*Note: Requires `OPENAI_API_KEY` in the `.env` file.*

---

## 5. Analytics & Multi-City Scaling
### `GET /api/v1/analytics/city-comparison`
### `GET /api/v1/analytics/compliance-efficacy`

**Overview:** 
These REST endpoints interface with the `TinyDB` NoSQL document store (`analytics_database.json`). They bypass the need for a dedicated MongoDB server while preserving strict document-based querying.
- `city-comparison` returns aggregated AQI and compliance rates for New Delhi, Mumbai, and Bangalore.
- `compliance-efficacy` returns historical logs of AI enforcement interventions and measures the percentage drop in AQI post-intervention to prove the platform's real-world value.
