"""Site model helpers."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class SiteModel:
    address: str
    zone: str
    overlays: list[str] = field(default_factory=list)
    centroid: dict[str, float] = field(default_factory=dict)
    polygon_wgs84: list[list[float]] = field(default_factory=list)
    area_sqm: float = 0.0
    local_footprint_m: list[list[float]] = field(default_factory=list)
    setbacks_m: dict[str, float] = field(default_factory=dict)
    height_limit_m: float = 0.0
    surrounding: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def buildable_footprint(
        self,
        setbacks: dict[str, float] | None = None,
    ) -> list[list[float]]:
        """Shrink axis-aligned local footprint by setbacks (front/back/left/right)."""
        sb = setbacks or self.setbacks_m or {
            "front": 0,
            "back": 3,
            "left": 0,
            "right": 0,
        }
        fp = self.local_footprint_m
        if len(fp) < 3:
            return fp
        xs = [p[0] for p in fp]
        ys = [p[1] for p in fp]
        minx, maxx = min(xs) + sb.get("left", 0), max(xs) - sb.get("right", 0)
        miny, maxy = min(ys) + sb.get("back", 0), max(ys) - sb.get("front", 0)
        if maxx <= minx or maxy <= miny:
            return fp
        return [
            [minx, miny],
            [maxx, miny],
            [maxx, maxy],
            [minx, maxy],
            [minx, miny],
        ]
