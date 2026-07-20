import math
import osmnx as ox


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two coordinates using the Haversine formula.
    Returns distance in kilometers.
    """

    R = 6371

    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(d_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c, 2)


def get_nearby_sources(latitude, longitude, radius=2000):
    """
    Find nearby pollution-related sources from OpenStreetMap.
    """

    tags = {
        "landuse": ["industrial", "construction"],
        "building": "industrial",
        "amenity": [
            "waste_disposal",
            "recycling"
        ],
        "power": "plant",
        "highway": [
            "motorway",
            "trunk",
            "primary"
        ]
    }

    gdf = ox.features_from_point(
        (latitude, longitude),
        tags=tags,
        dist=radius
    )

    sources = {}

    for _, row in gdf.iterrows():

        geometry = row.geometry.centroid

        lat = geometry.y
        lon = geometry.x

        distance = calculate_distance(
            latitude,
            longitude,
            lat,
            lon
        )

        category = None

        if row.get("landuse") == "industrial":
            category = "Industry"

        elif row.get("landuse") == "construction":
            category = "Construction Site"

        elif row.get("building") == "industrial":
            category = "Industrial Building"

        elif row.get("amenity") == "waste_disposal":
            category = "Waste Disposal"

        elif row.get("amenity") == "recycling":
            category = "Recycling Facility"

        elif row.get("power") == "plant":
            category = "Power Plant"

        elif row.get("highway") in [
            "motorway",
            "trunk",
            "primary"
        ]:
            category = "Major Road"

        else:
            continue

        name = row.get("name")

        if name is None or str(name) == "nan":
            name = category

        key = (category, name)

        # Keep only the nearest occurrence
        if key not in sources or distance < sources[key]["distance_km"]:

            sources[key] = {
                "name": name,
                "category": category,
                "distance_km": distance,
                "latitude": round(lat, 6),
                "longitude": round(lon, 6)
            }

    result = list(sources.values())

    result.sort(key=lambda x: x["distance_km"])

    return result