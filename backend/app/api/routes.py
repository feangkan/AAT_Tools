"""API routes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from aat_core.brief.registry import load_brief, load_landscape
from aat_core.rules.engine import RulesEngine
from aat_core.knowledge.ingest import ingest_pdfs, KnowledgeBase
from aat_core.knowledge.rag import retrieve
from aat_core.data.vicmap import VicmapClient
from aat_core.data.osm import OSMClient
from aat_core.geometry.solar import solar_study, sun_position
from aat_core.generators.massing import generate_massing
from aat_core.generators.plans import generate_typical_floor, generate_ground_floor
from aat_core.generators.core_service import optimize_core_service

from app.services.planner import build_group_plan
from app.services.chatbot import chat as chatbot_chat
from app.services.a3_export import render_a3_pdf
from app.services.project_state import load_state, save_state, default_state
from app.services.details import structural_options, facade_templates, precedents_template
from app.services.revit_bridge import save_for_revit

router = APIRouter()
ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = ROOT / "data" / "projects" / "default_state.json"


# ---------- Brief / requirements ----------
@router.get("/brief")
def get_brief():
    brief = load_brief()
    return {"summary": brief.summary(), "raw": brief.raw}


@router.get("/brief/deliverables")
def get_deliverables():
    return {"deliverables": [d.model_dump() for d in load_brief().deliverables]}


@router.get("/landscape")
def get_landscape():
    return load_landscape()


# ---------- Project state ----------
@router.get("/state")
def get_state():
    return load_state(STATE_PATH)


class StateUpdate(BaseModel):
    state: dict[str, Any]


@router.put("/state")
def put_state(body: StateUpdate):
    save_state(STATE_PATH, body.state)
    return {"ok": True, "state": body.state}


@router.post("/state/reset")
def reset_state():
    state = default_state()
    save_state(STATE_PATH, state)
    return state


# ---------- Group planner ----------
class PlannerRequest(BaseModel):
    members: list[str] = Field(default_factory=lambda: ["Member A", "Member B", "Member C"])


@router.post("/planner")
def planner(body: PlannerRequest):
    return build_group_plan(load_brief(), body.members)


# ---------- Inspector ----------
class InspectRequest(BaseModel):
    state: dict[str, Any] | None = None


@router.post("/inspect")
def inspect(body: InspectRequest):
    state = body.state or load_state(STATE_PATH)
    report = RulesEngine().evaluate(state)
    return report.to_dict()


# ---------- Site / solar ----------
@router.get("/site/planning")
def site_planning(lat: float = -37.7995, lon: float = 144.9005):
    return VicmapClient().site_planning_pack(lon, lat)


@router.get("/site/context")
def site_context(lat: float = -37.7995, lon: float = 144.9005, radius_m: int = 150):
    return OSMClient().buildings_near(lat, lon, radius_m)


class SolarRequest(BaseModel):
    footprint: list[list[float]]
    height_m: float = 32.0
    date: str = "2026-06-22"
    lat: float = -37.7995
    lon: float = 144.9005


@router.post("/site/solar")
def site_solar(body: SolarRequest):
    return solar_study(
        body.footprint,
        body.height_m,
        lat=body.lat,
        lon=body.lon,
        date=body.date,
    )


@router.get("/site/sun")
def site_sun(hour: int = 12, date: str = "2026-06-22"):
    from datetime import datetime, timezone, timedelta

    y, m, d = map(int, date.split("-"))
    dt = datetime(y, m, d, hour, 0, tzinfo=timezone(timedelta(hours=10)))
    return sun_position(dt)


# ---------- Generators ----------
class MassingRequest(BaseModel):
    site_footprint_m: list[list[float]] = Field(
        default_factory=lambda: [[0, 0], [50, 0], [50, 56], [0, 56], [0, 0]]
    )
    storeys: int = 10
    floor_to_floor_m: float = 3.2
    podium_storeys: int = 2
    setbacks_m: dict[str, float] = Field(
        default_factory=lambda: {"front": 0, "back": 3, "left": 0, "right": 0}
    )
    seed: int = 42
    height_limit_m: float | None = 45.0
    plot_ratio: float | None = None


@router.post("/generate/massing")
def gen_massing(body: MassingRequest):
    result = generate_massing(
        body.site_footprint_m,
        storeys=body.storeys,
        floor_to_floor_m=body.floor_to_floor_m,
        podium_storeys=body.podium_storeys,
        setbacks_m=body.setbacks_m,
        seed=body.seed,
        height_limit_m=body.height_limit_m,
        plot_ratio=body.plot_ratio,
    )
    save_for_revit("massing", result)
    return result


class TypicalFloorRequest(BaseModel):
    plate_width_m: float = 36.0
    plate_depth_m: float = 18.0
    seed: int = 42
    difference_rule: str = "mirror"
    hierarchy: str = "public-communal-private"
    floor_index: int = 1


@router.post("/generate/typical-floor")
def gen_typical(body: TypicalFloorRequest):
    result = generate_typical_floor(
        plate_width_m=body.plate_width_m,
        plate_depth_m=body.plate_depth_m,
        seed=body.seed,
        difference_rule=body.difference_rule,
        hierarchy=body.hierarchy,
        floor_index=body.floor_index,
    )
    save_for_revit("typical_floor", result)
    return result


class GroundFloorRequest(BaseModel):
    site_width_m: float = 50.0
    site_depth_m: float = 56.0
    seed: int = 42
    open_space_pct_target: float = 50.0


@router.post("/generate/ground-floor")
def gen_ground(body: GroundFloorRequest):
    result = generate_ground_floor(
        site_width_m=body.site_width_m,
        site_depth_m=body.site_depth_m,
        seed=body.seed,
        open_space_pct_target=body.open_space_pct_target,
    )
    save_for_revit("ground_floor", result)
    return result


class CoreRequest(BaseModel):
    unit_count: int = 200
    storeys: int = 10
    units_per_floor: int = 20
    plate_width_m: float = 36.0
    plate_depth_m: float = 18.0
    provide_parking: bool = False
    parking_spaces: int = 0


@router.post("/generate/core-service")
def gen_core(body: CoreRequest):
    return optimize_core_service(**body.model_dump())


# ---------- Knowledge / chatbot ----------
@router.post("/knowledge/ingest")
def knowledge_ingest():
    kb = ingest_pdfs()
    return {"chunk_count": len(kb.chunks), "index": str(kb.index_path)}


@router.get("/knowledge/search")
def knowledge_search(q: str, limit: int = 6):
    return {"query": q, "hits": retrieve(q, limit=limit)}


class ChatRequest(BaseModel):
    message: str
    provider: str = "offline"
    api_key: str | None = None
    model: str | None = None


@router.post("/chat")
def chat(body: ChatRequest):
    return chatbot_chat(
        body.message,
        provider=body.provider,
        api_key=body.api_key,
        model=body.model,
    )


# ---------- Details / precedents / Country ----------
@router.get("/details/structure")
def details_structure():
    return structural_options()


@router.get("/details/facade")
def details_facade():
    return facade_templates()


@router.get("/precedents/template")
def precedents():
    return precedents_template()


# ---------- A3 export ----------
class A3Request(BaseModel):
    title: str
    subtitle: str = ""
    sheets: list[dict[str, Any]]
    members: list[str] = Field(default_factory=list)
    filename: str = "aat_folio.pdf"


@router.post("/export/a3")
def export_a3(body: A3Request):
    out = ROOT / "data" / "projects" / "exports"
    out.mkdir(parents=True, exist_ok=True)
    path = out / body.filename
    render_a3_pdf(
        path,
        title=body.title,
        subtitle=body.subtitle,
        sheets=body.sheets,
        members=body.members,
    )
    return {"ok": True, "path": str(path.relative_to(ROOT))}
