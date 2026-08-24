"""Typical student accommodation floor + ground floor generators."""

from __future__ import annotations

import random
from typing import Any


def generate_typical_floor(
    *,
    plate_width_m: float = 36.0,
    plate_depth_m: float = 18.0,
    studio_target_sqm: float = 20.0,
    dda_target_sqm: float = 32.0,
    corridor_width_m: float = 1.8,
    seed: int = 42,
    difference_rule: str = "mirror",
    hierarchy: str = "public-communal-private",
    floor_index: int = 1,
) -> dict[str, Any]:
    """
    Double-loaded corridor typical floor.
    difference_rule: mirror | shift | alternate
    hierarchy: influences lounge / core placement along public→private gradient
    """
    rng = random.Random(seed + floor_index * 17)
    rooms: list[dict[str, Any]] = []

    # Core block at centre
    core_w, core_d = 6.0, 8.0
    core_x = (plate_width_m - core_w) / 2
    core_y = (plate_depth_m - core_d) / 2
    if "communal" in hierarchy:
        # nudge core slightly toward entry side (left)
        core_x = max(4.0, core_x - 2.0)

    rooms.append(
        {
            "id": "core",
            "type": "core",
            "label": "Lifts / Stairs / Risers",
            "x": round(core_x, 2),
            "y": round(core_y, 2),
            "w": core_w,
            "d": core_d,
            "area_sqm": round(core_w * core_d, 1),
        }
    )
    rooms.append(
        {
            "id": "corridor",
            "type": "corridor",
            "label": "Corridor",
            "x": 0,
            "y": round((plate_depth_m - corridor_width_m) / 2, 2),
            "w": plate_width_m,
            "d": corridor_width_m,
            "area_sqm": round(plate_width_m * corridor_width_m, 1),
        }
    )

    # Unit bands north and south of corridor
    band_depth = (plate_depth_m - corridor_width_m) / 2
    unit_depth = band_depth
    # Keep studio areas inside 15–25 sqm brief range
    max_width = min(4.2, 25.0 / max(unit_depth, 0.1))
    min_width = max(3.0, 15.0 / max(unit_depth, 0.1))
    unit_width = studio_target_sqm / max(unit_depth, 0.1)
    unit_width = max(min_width, min(max_width, unit_width))
    # slight variation by difference_rule (clamped)
    if difference_rule == "shift":
        unit_width += rng.uniform(-0.1, 0.1)
    elif difference_rule == "alternate" and floor_index % 2:
        unit_width += 0.1
    unit_width = max(min_width, min(max_width, unit_width))

    def place_band(y0: float, side: str) -> list[dict[str, Any]]:
        placed = []
        x = 0.5
        idx = 0
        while x + unit_width <= plate_width_m - 0.5:
            # skip core zone
            if not (x + unit_width < core_x - 0.3 or x > core_x + core_w + 0.3):
                x = core_x + core_w + 0.4
                continue
            is_dda = False
            w = unit_width
            area = w * unit_depth
            # DDA every 20th conceptually — place one DDA per band if enough units
            rooms_so_far = len([r for r in placed if r["type"] == "studio"])
            if rooms_so_far > 0 and (rooms_so_far + 1) % 10 == 0:
                is_dda = True
                w = dda_target_sqm / unit_depth
                area = w * unit_depth
            rtype = "dda" if is_dda else "studio"
            placed.append(
                {
                    "id": f"{side}-{idx}",
                    "type": rtype,
                    "label": "DDA Studio" if is_dda else "Studio",
                    "x": round(x, 2),
                    "y": round(y0, 2),
                    "w": round(w, 2),
                    "d": round(unit_depth, 2),
                    "area_sqm": round(area, 1),
                }
            )
            x += w + 0.15
            idx += 1
        return placed

    south = place_band(0, "S")
    north = place_band(plate_depth_m - band_depth, "N")
    if difference_rule == "mirror":
        # already roughly mirrored
        pass
    rooms.extend(south)
    rooms.extend(north)

    # Level lounge
    lounge_w, lounge_d = 5.0, 4.0
    rooms.append(
        {
            "id": "lounge",
            "type": "lounge",
            "label": "Level Lounge",
            "x": round(core_x + core_w + 0.5, 2),
            "y": round(core_y + 0.5, 2),
            "w": lounge_w,
            "d": lounge_d,
            "area_sqm": 20.0,
        }
    )

    studios = [r for r in rooms if r["type"] == "studio"]
    ddas = [r for r in rooms if r["type"] == "dda"]
    # Ensure DDA ratio ~1/20
    if studios and len(ddas) < max(1, round(len(studios) / 20)):
        # convert last studio to DDA
        studios[-1]["type"] = "dda"
        studios[-1]["label"] = "DDA Studio"
        studios[-1]["area_sqm"] = dda_target_sqm
        studios[-1]["w"] = round(dda_target_sqm / unit_depth, 2)
        ddas = [r for r in rooms if r["type"] == "dda"]
        studios = [r for r in rooms if r["type"] == "studio"]

    svg = _plan_svg(plate_width_m, plate_depth_m, rooms)
    return {
        "kind": "typical_floor",
        "seed": seed,
        "difference_rule": difference_rule,
        "hierarchy": hierarchy,
        "floor_index": floor_index,
        "plate": {"width_m": plate_width_m, "depth_m": plate_depth_m},
        "rooms": rooms,
        "metrics": {
            "studio_count": len(studios),
            "dda_count": len(ddas),
            "units_total": len(studios) + len(ddas),
            "dda_ratio_ok": len(ddas) >= max(1, round((len(studios) + len(ddas)) / 20))
            if studios
            else False,
            "avg_studio_sqm": round(
                sum(r["area_sqm"] for r in studios) / len(studios), 1
            )
            if studios
            else 0,
        },
        "svg": svg,
        "revit_json": {
            "level": f"L{floor_index}",
            "rooms": rooms,
            "plate": {"width_m": plate_width_m, "depth_m": plate_depth_m},
        },
    }


def generate_ground_floor(
    *,
    site_width_m: float = 50.0,
    site_depth_m: float = 56.0,
    seed: int = 42,
    open_space_pct_target: float = 50.0,
) -> dict[str, Any]:
    rng = random.Random(seed)
    site_area = site_width_m * site_depth_m
    build_area_target = site_area * (1 - open_space_pct_target / 100)
    build_w = site_width_m * 0.85
    build_d = build_area_target / build_w
    build_d = min(site_depth_m * 0.55, max(18.0, build_d))

    rooms: list[dict[str, Any]] = []
    x = 1.0
    # Lobby
    rooms.append(
        {
            "id": "lobby",
            "type": "lobby",
            "label": "Lobby",
            "x": x,
            "y": 1.0,
            "w": 10,
            "d": 8,
            "area_sqm": 80,
        }
    )
    x += 11
    # Retail strip
    retail_w = build_w - 22
    rooms.append(
        {
            "id": "retail",
            "type": "retail",
            "label": "Retail / Café",
            "x": x,
            "y": 1.0,
            "w": round(retail_w, 1),
            "d": 8,
            "area_sqm": round(retail_w * 8, 1),
        }
    )
    # Core
    rooms.append(
        {
            "id": "core",
            "type": "core",
            "label": "Core",
            "x": build_w / 2 - 3,
            "y": 10,
            "w": 6,
            "d": 8,
            "area_sqm": 48,
        }
    )
    # Refuse / mail / loading / services along back
    rooms.append(
        {
            "id": "refuse",
            "type": "refuse",
            "label": "Refuse",
            "x": 1,
            "y": build_d - 7,
            "w": 10,
            "d": 5.5,
            "area_sqm": 55,
        }
    )
    rooms.append(
        {
            "id": "mail",
            "type": "mail",
            "label": "Mail / Parcel",
            "x": 12,
            "y": build_d - 7,
            "w": 7,
            "d": 5,
            "area_sqm": 35,
        }
    )
    rooms.append(
        {
            "id": "loading",
            "type": "loading",
            "label": "Loading",
            "x": 20,
            "y": build_d - 8,
            "w": 12,
            "d": 6,
            "area_sqm": 72,
        }
    )
    rooms.append(
        {
            "id": "services",
            "type": "services",
            "label": "Services",
            "x": build_w - 9,
            "y": build_d - 7,
            "w": 8,
            "d": 5,
            "area_sqm": 40,
        }
    )

    # Communal stacked above typically — mark gym/study footprints optionally on podium
    rooms.append(
        {
            "id": "open_space",
            "type": "open_space",
            "label": "Public Open Space / Native Landscape",
            "x": 0,
            "y": build_d + 1,
            "w": site_width_m,
            "d": site_depth_m - build_d - 1,
            "area_sqm": round(site_width_m * (site_depth_m - build_d - 1), 1),
        }
    )

    built = sum(r["area_sqm"] for r in rooms if r["type"] != "open_space")
    open_sqm = site_area - build_w * build_d
    open_pct = 100 * open_sqm / site_area

    return {
        "kind": "ground_floor",
        "seed": seed,
        "site": {
            "width_m": site_width_m,
            "depth_m": site_depth_m,
            "area_sqm": round(site_area, 1),
        },
        "building_plate": {
            "width_m": round(build_w, 1),
            "depth_m": round(build_d, 1),
            "area_sqm": round(build_w * build_d, 1),
        },
        "rooms": rooms,
        "metrics": {
            "built_program_sqm": round(built, 1),
            "ground_open_space_pct": round(open_pct, 1),
            "open_space_target_pct": open_space_pct_target,
            "open_space_ok": open_pct >= open_space_pct_target - 0.5,
        },
        "svg": _plan_svg(site_width_m, site_depth_m, rooms),
        "revit_json": {
            "level": "GF",
            "rooms": rooms,
            "site": {"width_m": site_width_m, "depth_m": site_depth_m},
        },
    }


_COLORS = {
    "studio": "#cfe8ff",
    "dda": "#ffe0b2",
    "corridor": "#eeeeee",
    "core": "#b0bec5",
    "lounge": "#d7f5d7",
    "lobby": "#fff9c4",
    "retail": "#f8bbd0",
    "refuse": "#d7ccc8",
    "mail": "#d7ccc8",
    "loading": "#d7ccc8",
    "services": "#cfd8dc",
    "open_space": "#c8e6c9",
}


def _plan_svg(width: float, depth: float, rooms: list[dict[str, Any]]) -> str:
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 {width+4} {depth+4}" width="900" height="600">',
        f'<rect x="0" y="0" width="{width}" height="{depth}" fill="#fafafa" stroke="#333" stroke-width="0.15"/>',
    ]
    for r in rooms:
        fill = _COLORS.get(r["type"], "#ddd")
        parts.append(
            f'<rect x="{r["x"]}" y="{r["y"]}" width="{r["w"]}" height="{r["d"]}" '
            f'fill="{fill}" stroke="#222" stroke-width="0.08"/>'
        )
        parts.append(
            f'<text x="{r["x"] + r["w"]/2}" y="{r["y"] + r["d"]/2}" '
            f'font-size="0.9" text-anchor="middle" dominant-baseline="middle" fill="#111">'
            f'{r["label"]}</text>'
        )
    parts.append("</svg>")
    return "".join(parts)
