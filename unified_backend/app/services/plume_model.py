from geopy.distance import geodesic

def generate_plume_geojson(lat: float, lon: float, wind_speed_ms: float, wind_dir_deg: float, aqi: float) -> dict:
    """
    Generates a GeoJSON Polygon representing a pollution plume dispersion
    based on live wind speed and wind direction.
    """
    # Wind direction is where wind comes FROM. Plume blows TOWARDS (wind_dir + 180).
    plume_bearing = (wind_dir_deg + 180) % 360
    
    # Plume length based on wind speed (e.g., 2 m/s -> 4 km length)
    length_km = max(1.0, wind_speed_ms * 2.0)
    
    # Spread angle of the plume (wider if wind is slow, narrower if fast)
    spread_deg = max(15.0, 45.0 - (wind_speed_ms * 3.0))
    
    origin = (lat, lon)
    
    # Calculate the points of the polygon (Origin -> Left edge -> Center tip -> Right edge -> Origin)
    left_bearing = (plume_bearing - spread_deg) % 360
    right_bearing = (plume_bearing + spread_deg) % 360
    
    pt_left = geodesic(kilometers=length_km).destination(origin, left_bearing)
    pt_center = geodesic(kilometers=length_km * 1.1).destination(origin, plume_bearing)
    pt_right = geodesic(kilometers=length_km).destination(origin, right_bearing)
    
    return {
        "type": "Feature",
        "properties": {
            "forecast_aqi": round(aqi, 2),
            "wind_speed_ms": wind_speed_ms,
            "wind_direction_deg": wind_dir_deg,
            "risk_level": "SEVERE" if aqi > 300 else "HIGH" if aqi > 200 else "MODERATE" if aqi > 100 else "LOW"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [lon, lat], # Origin (GeoJSON format is Longitude, Latitude)
                [pt_left.longitude, pt_left.latitude],
                [pt_center.longitude, pt_center.latitude],
                [pt_right.longitude, pt_right.latitude],
                [lon, lat]  # Close polygon
            ]]
        }
    }
