def calculate_source_score(source, current_aqi, forecast_aqi, traffic_pct=0.0, industrial_pct=0.0, biomass_pct=0.0):
    """
    Calculate the likelihood score of a pollution source.
    """

    score = 0

    # Base score based on source type
    category_scores = {
        "Industry": 50,
        "Industrial Building": 45,
        "Power Plant": 45,
        "Construction Site": 35,
        "Waste Disposal": 30,
        "Recycling Facility": 20,
        "Major Road": 25,
    }

    score += category_scores.get(source["category"], 10)

    # AI Source Attribution Boost
    if source["category"] in ["Industry", "Industrial Building", "Power Plant"]:
        score += (industrial_pct * 100) * 0.5  # Up to 50 points boost
    elif source["category"] == "Major Road":
        score += (traffic_pct * 100) * 0.5
    elif source["category"] in ["Waste Disposal", "Recycling Facility", "Construction Site"]:
        score += (biomass_pct * 100) * 0.5

    # Distance factor
    distance = source["distance_km"]

    if distance <= 0.5:
        score += 35

    elif distance <= 1:
        score += 30

    elif distance <= 2:
        score += 20

    elif distance <= 5:
        score += 10

    # AQI Severity
    if current_aqi >= 300:
        score += 20

    elif current_aqi >= 200:
        score += 15

    elif current_aqi >= 150:
        score += 10

    # Forecast Trend
    if forecast_aqi > current_aqi:
        score += 10

    elif forecast_aqi < current_aqi:
        score -= 5

    score = min(score, 100)

    return score


def rank_pollution_sources(sources, current_aqi, forecast_aqi, traffic_pct=0.0, industrial_pct=0.0, biomass_pct=0.0):
    """
    Rank pollution sources according to calculated score.
    """

    ranked = []

    for source in sources:

        source["score"] = calculate_source_score(
            source,
            current_aqi,
            forecast_aqi,
            traffic_pct,
            industrial_pct,
            biomass_pct
        )

        ranked.append(source)

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked