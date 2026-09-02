"""Persisted project state for Inspector loop."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def default_state() -> dict[str, Any]:
    return {
        "unit_count": 200,
        "units_per_floor": 20,
        "dda_per_floor": 1,
        "studio_sizes_sqm": [20] * 19,
        "floor_to_ceiling_m": 2.7,
        "ground_open_space_pct": 52,
        "exit_count": 2,
        "max_travel_distance_m": 32,
        "classification": {"primary": "Class 3", "retail": "Class 6", "dda": "Class 3"},
        "zone": "ACZ1",
        "building_height_m": 32,
        "height_limit_m": 45,
        "min_building_separation_m": 6,
        "single_massing": True,
        "communal_os_winter_sun_hours": 2.5,
        "min_door_clear_mm": 850,
        "communal": {
            "kitchen_dining_sqm": 130,
            "gym_sqm": 90,
            "laundry_sqm": 35,
            "study_sqm": 100,
        },
        "parking": {"provided": False},
        "storeys": 10,
    }


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        state = default_state()
        save_state(path, state)
        return state
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
