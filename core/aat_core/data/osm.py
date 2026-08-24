"""OpenStreetMap Overpass client for surrounding building footprints."""

from __future__ import annotations

from typing import Any

import httpx

OVERPASS = "https://overpass-api.de/api/interpreter"

# Curated nearby context if Overpass blocked
FOOTSCRAY_CONTEXT = [
    {
        "name": "Nicholson Street frontage",
        "type": "road",
        "note": "Primary street address / retail activation",
    },
    {
        "name": "Footscray activity centre context",
        "type": "context",
        "note": "Mixed-use mid-rise, Little Saigon market memory, multicultural precinct",
    },
]


class OSMClient:
    def __init__(self, timeout: float = 20.0):
        self.timeout = timeout

    def buildings_near(self, lat: float, lon: float, radius_m: int = 150) -> dict[str, Any]:
        query = f"""
        [out:json][timeout:15];
        (
          way["building"](around:{radius_m},{lat},{lon});
          relation["building"](around:{radius_m},{lat},{lon});
        );
        out tags center 30;
        """
        try:
            with httpx.Client(timeout=self.timeout) as client:
                r = client.post(OVERPASS, data={"data": query})
                r.raise_for_status()
                data = r.json()
            elements = []
            for el in data.get("elements", []):
                center = el.get("center") or {}
                tags = el.get("tags") or {}
                elements.append(
                    {
                        "id": el.get("id"),
                        "name": tags.get("name") or tags.get("building"),
                        "building": tags.get("building"),
                        "levels": tags.get("building:levels"),
                        "lat": center.get("lat"),
                        "lon": center.get("lon"),
                    }
                )
            return {
                "source": "openstreetmap-overpass",
                "count": len(elements),
                "buildings": elements,
                "attribution": "© OpenStreetMap contributors ODbL",
            }
        except Exception as exc:
            return {
                "source": "fallback-curated",
                "count": len(FOOTSCRAY_CONTEXT),
                "buildings": FOOTSCRAY_CONTEXT,
                "error": str(exc),
                "attribution": "Curated context (live OSM unavailable)",
            }
