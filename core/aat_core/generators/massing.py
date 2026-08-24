"""Parametric massing generator with seed + ACZ1 planning controls."""

from __future__ import annotations

import math
import random
from typing import Any

from aat_core.planning.acz1 import resolve_massing_params


def _rect(cx: float, cy: float, w: float, d: float) -> list[list[float]]:
    hw, hd = w / 2, d / 2
    return [
        [cx - hw, cy - hd],
        [cx + hw, cy - hd],
        [cx + hw, cy + hd],
        [cx - hw, cy + hd],
        [cx - hw, cy - hd],
    ]


def generate_massing(
    site_footprint_m: list[list[float]],
    *,
    storeys: int | None = None,
    floor_to_floor_m: float = 3.2,
    podium_storeys: int | None = None,
    setbacks_m: dict[str, float] | None = None,
    plot_ratio: float | None = None,
    seed: int = 42,
    height_limit_m: float | None = None,
    precinct_id: str | None = "1B",
    ground_open_space_pct_target: float = 50.0,
    use_planning_controls: bool = True,
) -> dict[str, Any]:
    """
    Generate podium + tower massing inside site footprint.
    Coordinates are local metres (x east, y north). Front street = max y.

    When use_planning_controls=True (default), caps height/storeys/podium to
    Maribyrnong ACZ1 sub-precinct rules (default 1B — Nicholson St corridor).
    """
    rng = random.Random(seed)
    setbacks_m = dict(setbacks_m or {"front": 0.0, "back": 3.0, "left": 0.0, "right": 0.0})

    planning: dict[str, Any] | None = None
    if use_planning_controls:
        planning = resolve_massing_params(
            precinct_id=precinct_id,
            storeys=storeys,
            floor_to_floor_m=floor_to_floor_m,
            podium_storeys=podium_storeys,
            height_limit_m=height_limit_m,
            ground_open_space_pct_target=ground_open_space_pct_target,
        )
        storeys = planning["storeys"]
        podium_storeys = planning["podium_storeys"]
        height_limit_m = planning["height_limit_m"]
        ground_open_space_pct_target = planning["ground_open_space_pct_target"]
    else:
        storeys = storeys if storeys is not None else 10
        podium_storeys = podium_storeys if podium_storeys is not None else 2

    xs = [p[0] for p in site_footprint_m]
    ys = [p[1] for p in site_footprint_m]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    site_w, site_d = maxx - minx, maxy - miny
    site_area = abs(site_w * site_d)

    # Buildable box after site setbacks
    bx0 = minx + setbacks_m.get("left", 0)
    bx1 = maxx - setbacks_m.get("right", 0)
    by0 = miny + setbacks_m.get("back", 0)
    by1 = maxy - setbacks_m.get("front", 0)
    build_w = max(8.0, bx1 - bx0)
    build_d = max(8.0, by1 - by0)

    # Brief + ACZ1: retain ≥50% ground as open space → podium footprint cap
    max_podium_area = site_area * (1 - ground_open_space_pct_target / 100)
    podium_w = min(build_w, math.sqrt(max_podium_area * (build_w / max(build_d, 1))))
    podium_d = min(build_d, max_podium_area / max(podium_w, 1))
    podium_w *= 0.9 + 0.1 * rng.random()
    podium_d *= 0.9 + 0.1 * rng.random()
    if podium_w * podium_d > max_podium_area:
        scale = math.sqrt(max_podium_area / (podium_w * podium_d))
        podium_w *= scale
        podium_d *= scale

    cx = (bx0 + bx1) / 2 + rng.uniform(-2, 2)
    cy = (by0 + by1) / 2 + rng.uniform(-2, 2)
    # Bias podium toward street (front = max y)
    cy = min(by1 - podium_d / 2, max(by0 + podium_d / 2, cy + 2))

    podium_fp = _rect(cx, cy, podium_w, podium_d)

    # Tower: inset from podium; ACZ1 centre-wide 5 m tower setback from street
    tower_ratio = 0.55 + 0.15 * rng.random()
    tower_w = podium_w * tower_ratio
    tower_d = podium_d * tower_ratio
    tower_cx = cx + rng.uniform(-podium_w * 0.1, podium_w * 0.1)

    tower_street_setback = 0.0
    upper_street_setback = 0.0
    if planning:
        tower_street_setback = planning.get("tower_street_setback_m") or 0.0
        upper = planning.get("upper_level_street_setback_m")
        from_level = planning.get("upper_setback_from_level")
        if upper and from_level and storeys > from_level:
            upper_street_setback = upper

    street_setback = max(tower_street_setback, upper_street_setback)
    # Pull tower back from front (max y) edge of buildable / podium
    front_y = cy + podium_d / 2
    max_tower_front = front_y - street_setback
    tower_cy = min(max_tower_front - tower_d / 2, cy + rng.uniform(0, podium_d * 0.1))
    tower_cy = max(by0 + tower_d / 2, tower_cy)
    tower_fp = _rect(tower_cx, tower_cy, tower_w, tower_d)

    total_height = storeys * floor_to_floor_m
    if height_limit_m and total_height > height_limit_m + 0.05:
        storeys = max(1, int(round(height_limit_m / floor_to_floor_m)))
        total_height = storeys * floor_to_floor_m

    podium_height = min(podium_storeys, storeys) * floor_to_floor_m
    tower_storeys = max(0, storeys - podium_storeys)
    tower_height = tower_storeys * floor_to_floor_m

    gfa = podium_w * podium_d * min(podium_storeys, storeys) + tower_w * tower_d * tower_storeys
    target_gfa = plot_ratio * site_area if plot_ratio else None

    open_space_pct = max(0, 100 * (1 - (podium_w * podium_d) / max(site_area, 1)))

    result: dict[str, Any] = {
        "seed": seed,
        "site": {
            "footprint": site_footprint_m,
            "area_sqm": round(site_area, 1),
            "width_m": round(site_w, 2),
            "depth_m": round(site_d, 2),
        },
        "setbacks_m": setbacks_m,
        "storeys": storeys,
        "floor_to_floor_m": floor_to_floor_m,
        "height_m": round(total_height, 2),
        "height_limit_m": height_limit_m,
        "podium": {
            "storeys": min(podium_storeys, storeys),
            "height_m": round(podium_height, 2),
            "footprint": [[round(x, 2), round(y, 2)] for x, y in podium_fp],
            "area_sqm": round(podium_w * podium_d, 1),
        },
        "tower": {
            "storeys": tower_storeys,
            "height_m": round(tower_height, 2),
            "footprint": [[round(x, 2), round(y, 2)] for x, y in tower_fp],
            "area_sqm": round(tower_w * tower_d, 1),
            "street_setback_m": round(street_setback, 2),
        },
        "metrics": {
            "gfa_approx_sqm": round(gfa, 1),
            "plot_ratio_achieved": round(gfa / site_area, 2) if site_area else 0,
            "target_plot_ratio": plot_ratio,
            "ground_open_space_pct": round(open_space_pct, 1),
            "ground_open_space_target_pct": ground_open_space_pct_target,
        },
        "svg": _massing_svg(site_footprint_m, podium_fp, tower_fp),
    }
    if planning:
        result["planning"] = {
            **planning,
            "tower_street_setback_applied_m": round(street_setback, 2),
        }
    return result


def _massing_svg(site, podium, tower) -> str:
    def poly(pts, fill, stroke="#111", sw=1.5):
        points = " ".join(f"{x},{ -y}" for x, y in pts)
        return f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

    all_pts = site + podium + tower
    xs = [p[0] for p in all_pts]
    ys = [p[1] for p in all_pts]
    minx, maxx = min(xs) - 5, max(xs) + 5
    miny, maxy = min(ys) - 5, max(ys) + 5
    w, h = maxx - minx, maxy - miny
    vb = f"{minx} {-maxy} {w} {h}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="800" height="600">'
        f"{poly(site, '#e8eef2', '#666', 1)}"
        f"{poly(podium, '#9fb7c9', '#1a1a1a', 2)}"
        f"{poly(tower, '#2c5f7a', '#1a1a1a', 2)}"
        f"</svg>"
    )
