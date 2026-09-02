"""Rules engine — NCC / BADS / LHD / AS / brief compliance checks."""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
RULES_PATH = ROOT / "data" / "rules" / "compliance_rules.json"


@dataclass
class CheckResult:
    id: str
    title: str
    status: str  # pass | fail | warn | info
    message: str
    severity: str = "mandatory"
    suggestion: str | None = None
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ComplianceReport:
    project_state: dict[str, Any]
    results: list[CheckResult]
    score: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_state": self.project_state,
            "results": [r.to_dict() for r in self.results],
            "score": self.score,
            "passed": sum(1 for r in self.results if r.status == "pass"),
            "failed": sum(1 for r in self.results if r.status == "fail"),
            "warnings": sum(1 for r in self.results if r.status == "warn"),
        }


class RulesEngine:
    def __init__(self, rules_path: Path | None = None):
        path = rules_path or RULES_PATH
        with open(path, encoding="utf-8") as f:
            self.rules = json.load(f)

    def evaluate(self, state: dict[str, Any]) -> ComplianceReport:
        results: list[CheckResult] = []
        results.extend(self._check_brief(state))
        results.extend(self._check_ncc(state))
        results.extend(self._check_bads(state))
        results.extend(self._check_lhd(state))
        results.extend(self._check_as(state))
        results.extend(self._check_planning(state))

        scored = [r for r in results if r.status in ("pass", "fail")]
        score = (
            100.0 * sum(1 for r in scored if r.status == "pass") / len(scored)
            if scored
            else 0.0
        )
        return ComplianceReport(project_state=state, results=results, score=round(score, 1))

    def _check_brief(self, state: dict[str, Any]) -> list[CheckResult]:
        out: list[CheckResult] = []
        units = int(state.get("unit_count", 0))
        if units >= 200:
            out.append(
                CheckResult(
                    "BRIEF-UNITS",
                    "Minimum unit count",
                    "pass",
                    f"{units} units ≥ 200 required.",
                    evidence={"unit_count": units},
                )
            )
        else:
            out.append(
                CheckResult(
                    "BRIEF-UNITS",
                    "Minimum unit count",
                    "fail",
                    f"{units} units < 200 required.",
                    suggestion=f"Add at least {200 - units} more studio units.",
                    evidence={"unit_count": units, "deficit": 200 - units},
                )
            )

        open_pct = float(state.get("ground_open_space_pct", 0))
        if open_pct >= 50:
            out.append(
                CheckResult(
                    "BRIEF-OPENSPACE",
                    "Ground-level public open space",
                    "pass",
                    f"{open_pct}% ≥ 50% required.",
                    evidence={"ground_open_space_pct": open_pct},
                )
            )
        else:
            out.append(
                CheckResult(
                    "BRIEF-OPENSPACE",
                    "Ground-level public open space",
                    "fail",
                    f"{open_pct}% < 50% required.",
                    suggestion="Increase ground-level open space / reduce podium footprint.",
                    evidence={"ground_open_space_pct": open_pct},
                )
            )

        communal = state.get("communal", {})
        kitchen = float(communal.get("kitchen_dining_sqm", 0))
        if 120 <= kitchen <= 150:
            out.append(
                CheckResult(
                    "BRIEF-COMMUNAL-KITCHEN",
                    "Communal kitchen/dining",
                    "pass",
                    f"{kitchen} sqm within 120–150.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "BRIEF-COMMUNAL-KITCHEN",
                    "Communal kitchen/dining",
                    "fail" if kitchen < 120 else "warn",
                    f"{kitchen} sqm outside 120–150 target.",
                    suggestion="Adjust communal kitchen/dining to 120–150 sqm.",
                )
            )

        gym = float(communal.get("gym_sqm", 0))
        if 80 <= gym <= 100:
            out.append(
                CheckResult(
                    "BRIEF-COMMUNAL-GYM",
                    "Gym",
                    "pass",
                    f"{gym} sqm within 80–100.",
                )
            )
        elif gym == 0:
            out.append(
                CheckResult(
                    "BRIEF-COMMUNAL-GYM",
                    "Gym",
                    "fail",
                    "Gym not provided.",
                    suggestion="Provide 80–100 sqm 24/7 gym with amenities.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "BRIEF-COMMUNAL-GYM",
                    "Gym",
                    "warn",
                    f"{gym} sqm outside 80–100 target.",
                    suggestion="Adjust gym to 80–100 sqm.",
                )
            )

        ftc = float(state.get("floor_to_ceiling_m", 0))
        if ftc >= 2.7:
            out.append(
                CheckResult(
                    "NCC-FTC",
                    "Floor-to-ceiling height",
                    "pass",
                    f"{ftc} m ≥ 2.7 m.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "NCC-FTC",
                    "Floor-to-ceiling height",
                    "fail",
                    f"{ftc} m < 2.7 m minimum.",
                    suggestion="Increase floor-to-ceiling to ≥ 2.7 m.",
                )
            )
        return out

    def _check_ncc(self, state: dict[str, Any]) -> list[CheckResult]:
        out: list[CheckResult] = []
        exits = int(state.get("exit_count", 0))
        if exits >= 2:
            out.append(
                CheckResult(
                    "NCC-D1-EXITS",
                    "Provision for escape — exits",
                    "pass",
                    f"{exits} exits provided (≥ 2).",
                )
            )
        else:
            out.append(
                CheckResult(
                    "NCC-D1-EXITS",
                    "Provision for escape — exits",
                    "fail",
                    f"Only {exits} exit(s); minimum 2 required for multi-storey Class 3.",
                    suggestion="Add a second fire-isolated stair / exit.",
                )
            )

        travel = float(state.get("max_travel_distance_m", 999))
        if travel <= 40:
            out.append(
                CheckResult(
                    "NCC-D1-TRAVEL",
                    "Travel distances to exits",
                    "pass",
                    f"Max travel {travel} m ≤ 40 m.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "NCC-D1-TRAVEL",
                    "Travel distances to exits",
                    "fail",
                    f"Max travel {travel} m exceeds 40 m DTS limit.",
                    suggestion="Reposition core / add intermediate exit to reduce travel distance.",
                )
            )

        classification = state.get("classification", {})
        primary = classification.get("primary")
        retail = classification.get("retail")
        if primary == "Class 3" and retail == "Class 6":
            out.append(
                CheckResult(
                    "NCC-A6-CLASS",
                    "Building classification",
                    "pass",
                    "AT1.4 lock: Class 3 lodging + Class 6 retail (A6G1 / A6G4 / A6G7).",
                    evidence=classification,
                )
            )
        elif primary == "Class 2":
            out.append(
                CheckResult(
                    "NCC-A6-CLASS",
                    "Building classification",
                    "warn",
                    "Primary Class 2 does not match the AT1.4 Class 3 lodging lock.",
                    suggestion="Keep Class 3 tower + Class 6 podium unless the tutor rejected AT1.4 Sheet 16.",
                    evidence=classification,
                )
            )
        else:
            out.append(
                CheckResult(
                    "NCC-A6-CLASS",
                    "Building classification",
                    "warn",
                    "Confirm Class 3 (lodging) / Class 6 (retail) as locked in AT1.4.",
                    suggestion="Document mixed classification in the AT2.1 NCC report.",
                    evidence=classification,
                )
            )
        return out

    def _check_bads(self, state: dict[str, Any]) -> list[CheckResult]:
        out: list[CheckResult] = []
        studio_sizes = state.get("studio_sizes_sqm", [])
        if studio_sizes:
            bad = [s for s in studio_sizes if s < 15 or s > 25]
            if not bad:
                out.append(
                    CheckResult(
                        "C58-SIZE",
                        "Studio dwelling sizes",
                        "pass",
                        f"All {len(studio_sizes)} studios within 15–25 sqm.",
                    )
                )
            else:
                out.append(
                    CheckResult(
                        "C58-SIZE",
                        "Studio dwelling sizes",
                        "fail",
                        f"{len(bad)} studios outside 15–25 sqm.",
                        suggestion="Resize non-compliant studios to 15–25 sqm.",
                    )
                )
        else:
            out.append(
                CheckResult(
                    "C58-SIZE",
                    "Studio dwelling sizes",
                    "info",
                    "No studio sizes provided yet.",
                )
            )

        sep = float(state.get("min_building_separation_m", 0))
        if sep >= 6 or state.get("single_massing", True):
            out.append(
                CheckResult(
                    "C58-SEPARATION",
                    "Building separation",
                    "pass",
                    "Separation OK (single massing or ≥ 6 m).",
                )
            )
        else:
            out.append(
                CheckResult(
                    "C58-SEPARATION",
                    "Building separation",
                    "fail",
                    f"Facing habitable separation {sep} m < 6 m.",
                    suggestion="Increase courtyard / wing separation to ≥ 6 m.",
                )
            )

        sun_hours = float(state.get("communal_os_winter_sun_hours", 0))
        if sun_hours >= 2:
            out.append(
                CheckResult(
                    "C58-COMMUNAL-OS",
                    "Communal open space sunlight",
                    "pass",
                    f"{sun_hours} h winter sun ≥ 2 h on 22 June.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "C58-COMMUNAL-OS",
                    "Communal open space sunlight",
                    "warn" if sun_hours > 0 else "fail",
                    f"{sun_hours} h winter sun < 2 h target.",
                    suggestion="Shift communal open space north / reduce overshadowing massing.",
                )
            )
        return out

    def _check_lhd(self, state: dict[str, Any]) -> list[CheckResult]:
        units_per_floor = int(state.get("units_per_floor", 0))
        dda_per_floor = int(state.get("dda_per_floor", 0))
        required = max(1, int(round(units_per_floor * 0.05))) if units_per_floor else 0
        if units_per_floor == 0:
            return [
                CheckResult(
                    "LHD-DDA-RATIO",
                    "DDA room provision",
                    "info",
                    "No per-floor unit count provided yet.",
                )
            ]
        if dda_per_floor >= required:
            return [
                CheckResult(
                    "LHD-DDA-RATIO",
                    "DDA room provision",
                    "pass",
                    f"{dda_per_floor} DDA room(s) / floor ≥ 1 per 20 units ({required} required).",
                )
            ]
        return [
            CheckResult(
                "LHD-DDA-RATIO",
                "DDA room provision",
                "fail",
                f"{dda_per_floor} DDA / floor < {required} required (1 per 20).",
                suggestion=f"Provide at least {required} DDA room(s) per typical floor.",
            )
        ]

    def _check_as(self, state: dict[str, Any]) -> list[CheckResult]:
        out: list[CheckResult] = []
        door = float(state.get("min_door_clear_mm", 0))
        if door >= 850:
            out.append(
                CheckResult(
                    "AS1428-ACCESS",
                    "Accessible door clearances",
                    "pass",
                    f"Min door clear {door} mm ≥ 850 mm.",
                )
            )
        elif door == 0:
            out.append(
                CheckResult(
                    "AS1428-ACCESS",
                    "Accessible door clearances",
                    "info",
                    "Door clearances not yet set.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "AS1428-ACCESS",
                    "Accessible door clearances",
                    "fail",
                    f"Min door clear {door} mm < 850 mm (AS1428.1).",
                    suggestion="Widen accessible doors to ≥ 850 mm clear opening.",
                )
            )

        parking = state.get("parking", {})
        if parking.get("provided") is False:
            out.append(
                CheckResult(
                    "AS2890-PARKING",
                    "Off-street parking",
                    "info",
                    "No parking provided — confirm Parking Overlay / reduction justification.",
                    suggestion="Document PO overlay response and bike storage instead.",
                )
            )
        elif parking:
            bay_w = float(parking.get("bay_width_m", 0))
            if bay_w >= 2.4:
                out.append(
                    CheckResult(
                        "AS2890-PARKING",
                        "Off-street parking",
                        "pass",
                        f"Bay width {bay_w} m ≥ 2.4 m.",
                    )
                )
            else:
                out.append(
                    CheckResult(
                        "AS2890-PARKING",
                        "Off-street parking",
                        "fail",
                        f"Bay width {bay_w} m < 2.4 m (AS2890.1).",
                        suggestion="Widen bays to AS2890.1 dimensions.",
                    )
                )
        return out

    def _check_planning(self, state: dict[str, Any]) -> list[CheckResult]:
        out: list[CheckResult] = []
        zone = state.get("zone", "")
        if zone.upper().startswith("ACZ"):
            out.append(
                CheckResult(
                    "PLAN-ZONE",
                    "Planning zone",
                    "pass",
                    f"Site in {zone} (Activity Centre Zone) — Clause 58 applies.",
                )
            )
        elif zone:
            out.append(
                CheckResult(
                    "PLAN-ZONE",
                    "Planning zone",
                    "warn",
                    f"Zone recorded as {zone}; confirm ACZ1 Footscray.",
                )
            )
        else:
            out.append(
                CheckResult(
                    "PLAN-ZONE",
                    "Planning zone",
                    "info",
                    "Zone not set — pull from Vicmap.",
                    suggestion="Run site analysis to fetch Vicmap zone/overlays.",
                )
            )

        height = float(state.get("building_height_m", 0))
        height_limit = float(state.get("height_limit_m", 0))
        if height_limit and height:
            if height <= height_limit:
                out.append(
                    CheckResult(
                        "PLAN-HEIGHT",
                        "Building height",
                        "pass",
                        f"{height} m ≤ limit {height_limit} m.",
                    )
                )
            else:
                out.append(
                    CheckResult(
                        "PLAN-HEIGHT",
                        "Building height",
                        "fail",
                        f"{height} m exceeds limit {height_limit} m.",
                        suggestion="Reduce storeys or justify variation in portfolio.",
                    )
                )
        return out
