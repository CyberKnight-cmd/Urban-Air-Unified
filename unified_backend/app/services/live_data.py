import requests
import pandas as pd
import datetime

def fetch_live_window(latitude: float, longitude: float) -> pd.DataFrame:
    """
    Fetches the last 7 days (168 hours) of live weather and air quality data 
    from Open-Meteo for the exact coordinate, bypassing the need for a CSV.
    """
    print(f"Fetching live sensor data for ({latitude}, {longitude})...")
    
    # 1. Fetch live Air Quality data
    aq_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide&past_days=7"
    aq_res = requests.get(aq_url).json()
    
    # 2. Fetch live Weather data
    wx_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,wind_direction_10m&past_days=7"
    wx_res = requests.get(wx_url).json()
    
    aq_df = pd.DataFrame(aq_res["hourly"])
    wx_df = pd.DataFrame(wx_res["hourly"])
    merged = pd.merge(aq_df, wx_df, on="time", how="inner")
    
    # 3. Combine into the dataframe schema expected by our ML pipeline
    df = pd.DataFrame({
        "Timestamp": pd.to_datetime(merged["time"]),
        "PM2.5 (µg/m³)": merged["pm2_5"],
        "PM10 (µg/m³)": merged["pm10"],
        "NO2 (µg/m³)": merged["nitrogen_dioxide"],
        "SO2 (µg/m³)": merged["sulphur_dioxide"],
        "CO (mg/m³)": merged["carbon_monoxide"],
        
        "AT (°C)": merged["temperature_2m"],
        "RH (%)": merged["relative_humidity_2m"],
        "WS (m/s)": merged["wind_speed_10m"],
        "WD (deg)": merged["wind_direction_10m"],
    })
    
    # Convert surface pressure from hPa to mmHg (the metric our XGBoost was trained on)
    df["BP (mmHg)"] = [p * 0.750062 if p is not None else 740.0 for p in merged["surface_pressure"]]
    
    # Fill variables not available in Open-Meteo with safe baseline 0s 
    # (The MissForest imputer or NMF logic will handle this gracefully)
    df["NOx (ppb)"] = 0.0
    df["Benzene (µg/m³)"] = 0.0
    df["Toluene (µg/m³)"] = 0.0
    
    # The XGBoost models expect fire data columns if fire_data_available=True
    df["fire_count_near"] = 0.0
    df["fire_frp_near"] = 0.0
    df["fire_count_far_upwind"] = 0.0
    df["fire_frp_far_upwind"] = 0.0
    
    df["Station"] = "Live_OpenMeteo_Node"
    
    # Forward fill any random missing hours, then ensure we have exactly 168 rows
    df = df.ffill().bfill().tail(168).reset_index(drop=True)
    return df
