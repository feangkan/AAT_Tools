#!/usr/bin/env python3
"""Smoke-test core generators and rules."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))

from aat_core.brief.registry import load_brief
from aat_core.rules.engine import RulesEngine
from aat_core.generators.massing import generate_massing
from aat_core.generators.plans import generate_typical_floor, generate_ground_floor
from aat_core.generators.core_service import optimize_core_service
from aat_core.geometry.solar import solar_study


def main():
    brief = load_brief()
    print("Brief:", brief.summary())

    site = [[0, 0], [50, 0], [50, 56], [0, 56], [0, 0]]
    mass = generate_massing(site, seed=7, precinct_id="1D")
    print("Massing height:", mass["height_m"], "open%", mass["metrics"]["ground_open_space_pct"], "precinct", mass["planning"]["precinct_id"])

    typ = generate_typical_floor(seed=7)
    print("Typical floor units:", typ["metrics"])

    gf = generate_ground_floor(seed=7)
    print("Ground open%:", gf["metrics"]["ground_open_space_pct"])

    core = optimize_core_service(unit_count=200, storeys=10)
    print("Lifts:", core["lifts"]["count"], "stairs:", core["stairs_exits"]["count"])

    solar = solar_study(mass["tower"]["footprint"], mass["height_m"])
    print("Solar samples:", len(solar["samples"]))

    state = {
        "unit_count": 200,
        "units_per_floor": typ["metrics"]["units_total"],
        "dda_per_floor": typ["metrics"]["dda_count"],
        "studio_sizes_sqm": [r["area_sqm"] for r in typ["rooms"] if r["type"] == "studio"],
        "floor_to_ceiling_m": 2.7,
        "ground_open_space_pct": gf["metrics"]["ground_open_space_pct"],
        "exit_count": core["stairs_exits"]["count"],
        "max_travel_distance_m": core["stairs_exits"]["max_travel_distance_est_m"],
        "classification": {"primary": "Class 2"},
        "zone": "ACZ1",
        "building_height_m": mass["height_m"],
        "height_limit_m": mass["height_limit_m"],
        "single_massing": True,
        "communal_os_winter_sun_hours": 2.5,
        "min_door_clear_mm": 850,
        "communal": {"kitchen_dining_sqm": 130, "gym_sqm": 90},
        "parking": {"provided": False},
    }
    report = RulesEngine().evaluate(state)
    print("Compliance score:", report.score, "fail:", sum(1 for r in report.results if r.status == "fail"))
    print("OK")


if __name__ == "__main__":
    main()
