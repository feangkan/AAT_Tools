"""Brief registry — machine-readable project requirements."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parents[3]
BRIEF_PATH = ROOT / "data" / "brief" / "project_brief.json"
LANDSCAPE_PATH = ROOT / "data" / "brief" / "indigenous_landscape.json"


class UnitType(BaseModel):
    id: str
    name: str
    min_sqm: float
    max_sqm: float
    target_sqm: float
    ratio: str | None = None
    ratio_value: float | None = None
    class_: str | None = Field(default=None, alias="class")

    model_config = {"populate_by_name": True}


class Deliverable(BaseModel):
    id: str
    name: str
    week: int
    task: str
    min_a3_pages: int
    format: str
    presentation_minutes: int | None = None
    note: str | None = None


class BriefRegistry(BaseModel):
    raw: dict[str, Any]

    @property
    def project(self) -> dict[str, Any]:
        return self.raw["project"]

    @property
    def site(self) -> dict[str, Any]:
        return self.raw["project"]["site"]

    @property
    def min_units(self) -> int:
        return int(self.raw["accommodation"]["min_units"])

    @property
    def floor_to_ceiling_m(self) -> float:
        return float(self.raw["accommodation"]["floor_to_ceiling_min_m"])

    @property
    def deliverables(self) -> list[Deliverable]:
        return [Deliverable(**d) for d in self.raw["deliverables"]]

    @property
    def unit_types(self) -> list[UnitType]:
        return [UnitType(**u) for u in self.raw["accommodation"]["unit_types"]]

    def communal_requirements(self) -> dict[str, Any]:
        return self.raw["communal"]

    def ground_floor_requirements(self) -> dict[str, Any]:
        return self.raw["ground_floor"]

    def services_allowances(self) -> dict[str, float]:
        return self.raw["services_allowances"]

    def summary(self) -> dict[str, Any]:
        return {
            "name": self.project["name"],
            "site": self.site["address"],
            "zone": self.site["zone"],
            "min_units": self.min_units,
            "ftc_m": self.floor_to_ceiling_m,
            "open_space_pct": self.raw["ground_floor"]["public_open_space_pct"],
            "deliverable_count": len(self.deliverables),
            "total_min_a3": sum(d.min_a3_pages for d in self.deliverables),
        }


def load_brief(path: Path | None = None) -> BriefRegistry:
    p = path or BRIEF_PATH
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    return BriefRegistry(raw=data)


def load_landscape(path: Path | None = None) -> dict[str, Any]:
    p = path or LANDSCAPE_PATH
    with open(p, encoding="utf-8") as f:
        return json.load(f)
