"""Core & service system optimizer — lifts, stairs, parking, fire clearance."""

from __future__ import annotations

import math
from typing import Any


def optimize_core_service(
    *,
    unit_count: int = 200,
    storeys: int = 10,
    units_per_floor: int = 20,
    plate_width_m: float = 36.0,
    plate_depth_m: float = 18.0,
    provide_parking: bool = False,
    parking_spaces: int = 0,
    population_per_unit: float = 1.2,
) -> dict[str, Any]:
    """Recommend lift core, stairs/egress, parking, risers for student accommodation."""
    population = int(math.ceil(unit_count * population_per_unit))

    # Lift traffic rule-of-thumb: ~1 lift per 60–90 units for residential; student slightly higher peak
    lifts = max(2, math.ceil(unit_count / 75))
    if storeys >= 12:
        lifts = max(lifts, 3)

    # Stairs / exits — NCC D1: minimum 2 for multi-storey Class 2
    stairs = 2
    if units_per_floor * 20 > 500:  # large plate proxy
        stairs = 3

    # Travel distance estimate — place cores to split plate
    # Assume double-loaded corridor with core central → max travel ~ half length
    max_travel = round(max(plate_width_m, plate_depth_m) / 2 + 4, 1)
    travel_ok = max_travel <= 40

    # Core footprint
    lift_shaft_each = 2.5 * 2.7  # m
    stair_each = 2.8 * 5.5
    riser_bank = 3.0 * 2.0
    core_area = lifts * lift_shaft_each + stairs * stair_each + riser_bank + 8  # lobbies

    # Fire clearance — corridor width
    corridor_width_m = 1.8 if population / storeys < 50 else 2.0

    # Services / duct allowance
    typical_floor_gfa = plate_width_m * plate_depth_m
    services_area = typical_floor_gfa * 0.05
    fire_duct_area = typical_floor_gfa * 0.10

    # Parking AS2890.1
    parking = {
        "provided": provide_parking,
        "spaces": parking_spaces,
        "bay_width_m": 2.4,
        "bay_length_m": 5.4,
        "aisle_width_m": 5.8,
        "note": "Confirm Parking Overlay rates; bike storage preferred for student housing.",
    }
    if provide_parking and parking_spaces:
        parking["approx_area_sqm"] = round(
            parking_spaces * (2.4 * 5.4 + 2.4 * 5.8 / 2), 1
        )

    # Recommended core position — centre-left for entry hierarchy
    core_placement = {
        "strategy": "central split with dual stairs at ends or paired at core",
        "recommended_xy_m": [
            round(plate_width_m / 2 - 3, 1),
            round(plate_depth_m / 2 - 4, 1),
        ],
        "secondary_stair": "remote stair if travel > 30 m",
    }

    suggestions = []
    if not travel_ok:
        suggestions.append(
            "Max estimated travel exceeds 40 m — add remote stair or shorten wing."
        )
    if lifts < 2:
        suggestions.append("Provide at least 2 lifts for redundancy.")
    if not provide_parking:
        suggestions.append(
            "Document PO overlay response; prioritise secure bike storage in basement/ground."
        )
    suggestions.append(
        f"Allocate ~{services_area:.0f} sqm (5%) services and ~{fire_duct_area:.0f} sqm (10%) fire/ducts per typical floor."
    )

    return {
        "inputs": {
            "unit_count": unit_count,
            "storeys": storeys,
            "units_per_floor": units_per_floor,
            "population_est": population,
        },
        "lifts": {
            "count": lifts,
            "rationale": "≈1 lift / 75 units, min 2; +1 if ≥12 storeys",
        },
        "stairs_exits": {
            "count": stairs,
            "min_exit_width_mm": 1000,
            "corridor_width_m": corridor_width_m,
            "max_travel_distance_est_m": max_travel,
            "travel_ok": travel_ok,
            "dead_end_limit_m": 20,
        },
        "core": {
            "approx_area_sqm": round(core_area, 1),
            "placement": core_placement,
            "includes": ["lifts", "fire stairs", "risers", "lobby"],
        },
        "services_allowances": {
            "services_pct": 5,
            "services_sqm_per_floor": round(services_area, 1),
            "fire_duct_pct": 10,
            "fire_duct_sqm_per_floor": round(fire_duct_area, 1),
        },
        "parking": parking,
        "fire_clearance": {
            "rated_stairs": True,
            "travel_distance_limit_m": 40,
            "recommendation": "Fire-isolated stairs discharging to open space / street",
        },
        "suggestions": suggestions,
    }
