"""Save generator outputs as JSON for pyRevit consumption."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
EXPORT = ROOT / "data" / "projects" / "exports"


def save_for_revit(name: str, payload: dict[str, Any]) -> Path:
    EXPORT.mkdir(parents=True, exist_ok=True)
    path = EXPORT / f"{name}.json"
    # Prefer nested revit_json when present
    data = payload.get("revit_json") or payload
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data if name.endswith("floor") else payload, f, indent=2)
    return path
