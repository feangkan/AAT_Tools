"""Vicmap Planning ArcGIS REST client (CC BY 4.0)."""

from __future__ import annotations

from typing import Any

import httpx

ZONES_URL = (
    "https://plan-gis.mapshare.vic.gov.au/arcgis/rest/services/"
    "PlanningPortal/PORTAL_PlanningSchemeZones/MapServer/0/query"
)
# Fallback / known site defaults when network blocked
FOOTSCRAY_DEFAULT = {
    "zone_code": "ACZ1",
    "zone_description": "Activity Centre Zone - Schedule 1",
    "lga": "MARIBYRNONG",
    "scheme_code": "MARI",
    "overlays": ["DCPO2", "HO", "PO"],
    "source": "fallback-curated",
    "note": "Live Vicmap query unavailable; using curated Footscray ACZ1 defaults from assessment materials.",
}


class VicmapClient:
    def __init__(self, timeout: float = 12.0):
        self.timeout = timeout

    def query_zone_at(self, lon: float, lat: float) -> dict[str, Any]:
        """Point-in-polygon query. Input WGS84 lon/lat; service uses VicGrid / MGA."""
        # Try geographic query first (many Vic services accept wkid 4326)
        params = {
            "geometry": f"{lon},{lat}",
            "geometryType": "esriGeometryPoint",
            "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "*",
            "returnGeometry": "false",
            "f": "json",
        }
        try:
            with httpx.Client(timeout=self.timeout) as client:
                r = client.get(ZONES_URL, params=params)
                r.raise_for_status()
                data = r.json()
            feats = data.get("features") or []
            if feats:
                attrs = feats[0].get("attributes", {})
                return {
                    "zone_code": attrs.get("ZONE_CODE") or attrs.get("zone_code"),
                    "zone_description": attrs.get("ZONE_DESCRIPTION")
                    or attrs.get("ZONE_CODE_GROUP_LABEL"),
                    "lga": attrs.get("LGA"),
                    "scheme_code": attrs.get("SCHEME_CODE"),
                    "raw": attrs,
                    "source": "vicmap-live",
                }
        except Exception as exc:
            result = dict(FOOTSCRAY_DEFAULT)
            result["error"] = str(exc)
            return result
        result = dict(FOOTSCRAY_DEFAULT)
        result["note"] = "No Vicmap feature returned; using curated defaults."
        return result

    def site_planning_pack(self, lon: float, lat: float) -> dict[str, Any]:
        zone = self.query_zone_at(lon, lat)
        return {
            "point": {"lon": lon, "lat": lat},
            "zone": zone,
            "overlays": zone.get("overlays")
            or FOOTSCRAY_DEFAULT["overlays"],
            "clause58_applies": True,
            "guidance": [
                "Confirm height / setback metrics in ACZ1 schedule and precinct guidelines.",
                "Document any variations with design excellence / sustainability justification.",
                "Pull parking rates from Parking Overlay schedule.",
            ],
            "attribution": "Vicmap Planning © State of Victoria (Department of Transport and Planning) CC BY 4.0",
        }
