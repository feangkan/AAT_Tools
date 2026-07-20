"""Solar position and simple 2.5D shadow geometry for Melbourne / Footscray."""

from __future__ import annotations

import math
from datetime import datetime, timezone, timedelta
from typing import Any

# Melbourne / Footscray approximate
DEFAULT_LAT = -37.7995
DEFAULT_LON = 144.9005
AEST = timezone(timedelta(hours=10))


def _julian_day(dt: datetime) -> float:
    # Convert to UTC
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=AEST)
    utc = dt.astimezone(timezone.utc)
    a = (14 - utc.month) // 12
    y = utc.year + 4800 - a
    m = utc.month + 12 * a - 3
    jdn = utc.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    frac = (utc.hour - 12) / 24 + utc.minute / 1440 + utc.second / 86400
    return jdn + frac


def sun_position(
    dt: datetime,
    lat: float = DEFAULT_LAT,
    lon: float = DEFAULT_LON,
) -> dict[str, float]:
    """Return solar altitude / azimuth (degrees) using NOAA-style approximation."""
    jd = _julian_day(dt)
    n = jd - 2451545.0
    L = (280.460 + 0.9856474 * n) % 360
    g = math.radians((357.528 + 0.9856003 * n) % 360)
    lam = math.radians(L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g))
    ep = math.radians(23.439 - 0.0000004 * n)
    ra = math.atan2(math.cos(ep) * math.sin(lam), math.cos(lam))
    dec = math.asin(math.sin(ep) * math.sin(lam))
    gmst = (18.697374558 + 24.06570982441908 * n) % 24
    lst = (gmst + lon / 15.0) % 24
    ha = math.radians(lst * 15) - ra
    lat_r = math.radians(lat)
    alt = math.asin(
        math.sin(lat_r) * math.sin(dec) + math.cos(lat_r) * math.cos(dec) * math.cos(ha)
    )
    az = math.atan2(
        -math.sin(ha),
        math.tan(dec) * math.cos(lat_r) - math.sin(lat_r) * math.cos(ha),
    )
    return {
        "altitude_deg": math.degrees(alt),
        "azimuth_deg": (math.degrees(az) + 360) % 360,
        "altitude_rad": alt,
        "azimuth_rad": az,
    }


def shadow_polygon(
    footprint: list[list[float]],
    height_m: float,
    altitude_deg: float,
    azimuth_deg: float,
) -> list[list[float]]:
    """Project a building footprint shadow in local metres (x east, y north)."""
    if altitude_deg <= 1:
        # Sun below / near horizon — very long shadow; clamp
        length = height_m * 20
    else:
        length = height_m / math.tan(math.radians(altitude_deg))
    # Shadow direction is opposite to sun azimuth
    shadow_az = math.radians((azimuth_deg + 180) % 360)
    dx = length * math.sin(shadow_az)
    dy = length * math.cos(shadow_az)

    base = [(p[0], p[1]) for p in footprint]
    shifted = [(p[0] + dx, p[1] + dy) for p in base]
    # Convex-ish outline: walk base then reverse shifted
    outline = list(base) + list(reversed(shifted))
    return [[x, y] for x, y in outline]


def solar_study(
    footprint: list[list[float]],
    height_m: float,
    lat: float = DEFAULT_LAT,
    lon: float = DEFAULT_LON,
    date: str = "2026-06-22",
    hours: list[int] | None = None,
) -> dict[str, Any]:
    """Run hourly shadows for a date (default winter solstice)."""
    hours = hours or list(range(9, 16))
    year, month, day = map(int, date.split("-"))
    samples = []
    for h in hours:
        dt = datetime(year, month, day, h, 0, tzinfo=AEST)
        pos = sun_position(dt, lat, lon)
        shadow = None
        if pos["altitude_deg"] > 0:
            shadow = shadow_polygon(
                footprint, height_m, pos["altitude_deg"], pos["azimuth_deg"]
            )
        samples.append(
            {
                "time": dt.isoformat(),
                "hour": h,
                "sun": {
                    "altitude_deg": round(pos["altitude_deg"], 2),
                    "azimuth_deg": round(pos["azimuth_deg"], 2),
                },
                "shadow": shadow,
            }
        )
    sunny_hours = sum(1 for s in samples if s["sun"]["altitude_deg"] > 10)
    return {
        "date": date,
        "lat": lat,
        "lon": lon,
        "height_m": height_m,
        "footprint": footprint,
        "samples": samples,
        "sunny_hours_proxy": sunny_hours,
        "note": "2.5D planar shadow; use Revit for full 3D context shadows.",
    }
