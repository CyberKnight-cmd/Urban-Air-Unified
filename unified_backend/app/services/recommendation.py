def get_risk_level(current_aqi):
    """
    Determine risk level based on AQI.
    """

    if current_aqi >= 300:
        return "Severe"

    elif current_aqi >= 200:
        return "Very High"

    elif current_aqi >= 150:
        return "High"

    elif current_aqi >= 100:
        return "Moderate"

    return "Low"


def generate_recommendations(ranked_sources, current_aqi, forecast_aqi):
    """
    Generate enforcement recommendations based on ranked pollution sources.
    """

    recommendations = []

    top_sources = ranked_sources[:5]

    for source in top_sources:

        category = source["category"]

        if category == "Industry":
            recommendations.append(
                f"Inspect industrial facility '{source['name']}' for emission compliance."
            )

        elif category == "Industrial Building":
            recommendations.append(
                f"Audit industrial building '{source['name']}' for pollution control measures."
            )

        elif category == "Power Plant":
            recommendations.append(
                f"Verify stack emissions and pollution control systems at '{source['name']}'."
            )

        elif category == "Construction Site":
            recommendations.append(
                f"Inspect construction site '{source['name']}' for dust suppression compliance."
            )

        elif category == "Waste Disposal":
            recommendations.append(
                f"Inspect waste disposal site '{source['name']}' for open burning or improper waste handling."
            )

        elif category == "Recycling Facility":
            recommendations.append(
                f"Verify environmental compliance at recycling facility '{source['name']}'."
            )

        elif category == "Major Road":
            recommendations.append(
                f"Increase traffic emission monitoring near '{source['name']}'."
            )

    report = {
        "hotspot": {
            "current_aqi": current_aqi,
            "forecast_aqi": forecast_aqi,
            "risk_level": get_risk_level(current_aqi)
        },
        "top_sources": top_sources,
        "recommendations": recommendations
    }

    return report