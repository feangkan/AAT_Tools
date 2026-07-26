"""Maribyrnong ACZ1 planning controls for massing."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PRECICTS_PATH = ROOT / "data" / "planning" / "acz1_precincts.json"


def load_acz1_precincts() -> dict[str, Any]:
    with open(PRECICTS_PATH, encoding="utf-8") as f:
        return json.load(f)


def get_precinct(precinct_id: str) -> dict[str, Any]:
    data = load_acz1_precincts()
    precincts = data["precincts"]
    key = precinct_id.upper().replace(" ", "")
    if key not in precincts:
        raise KeyError(f"Unknown ACZ1 sub-precinct '{precinct_id}'. Known: {', '.join(sorted(precincts))}")
    return {**precincts[key], "id": key}


def resolve_massing_params(
    *,
    precinct_id: str | None = None,
    storeys: int | None = None,
    floor_to_floor_m: float = 3.2,
    podium_storeys: int | None = None,
    height_limit_m: float | None = None,
    ground_open_space_pct_target: float = 50.0,
) -> dict[str, Any]:
    """
    Map ACZ1 sub-precinct controls → massing generator inputs.
    Defaults to site_default_precinct (1B Nicholson corridor) when precinct_id omitted.
    """
    data = load_acz1_precincts()
    pid = (precinct_id or data["site_default_precinct"]).upper().replace(" ", "")
    p = get_precinct(pid)
    centre = data["centre_wide"]

    max_height = p["max_height_m"]
    max_storeys = p["max_storeys"]

    if height_limit_m is None:
        height_limit_m = max_height
    else:
        height_limit_m = min(height_limit_m, max_height)

    if storeys is None:
        storeys = max_storeys
    else:
        storeys = min(storeys, max_storeys)

    storeys = max(1, min(storeys, max_storeys, _storeys_for_height(height_limit_m, floor_to_floor_m)))

    if podium_storeys is None:
        podium_storeys = p.get("podium_storeys_default", 2)
    podium_storeys = max(
        p.get("street_wall_storeys_min", 2),
        min(podium_storeys, p.get("street_wall_storeys_max", 4), storeys),
    )

    tower_street_setback = centre.get("tower_setback_from_street_m", 5.0)
    upper_setback = p.get("upper_setback_from_street_m")
    upper_from_level = p.get("upper_setback_from_level")

    return {
        "precinct_id": pid,
        "precinct_name": p["name"],
        "storeys": storeys,
        "podium_storeys": podium_storeys,
        "floor_to_floor_m": floor_to_floor_m,
        "height_limit_m": height_limit_m,
        "max_storeys_scheme": max_storeys,
        "max_height_m_scheme": max_height,
        "tower_street_setback_m": tower_street_setback,
        "upper_level_street_setback_m": upper_setback,
        "upper_setback_from_level": upper_from_level,
        "ground_open_space_pct_target": max(
            ground_open_space_pct_target,
            centre.get("min_ground_open_space_pct_brief", 50),
        ),
        "source": data["source"],
        "scheme": data["scheme"],
    }


def _storeys_for_height(height_m: float, floor_to_floor_m: float) -> int:
    """Avoid float floor-division errors (e.g. 19.2 // 3.2 → 5 in Python)."""
    if floor_to_floor_m <= 0:
        return 1
    return max(1, int(round(height_m / floor_to_floor_m)))
