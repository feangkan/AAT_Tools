"""Backend tests."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))
sys.path.insert(0, str(ROOT / "backend"))

from aat_core.brief.registry import load_brief
from aat_core.rules.engine import RulesEngine
from aat_core.generators.massing import generate_massing
from aat_core.generators.plans import generate_typical_floor, generate_ground_floor
from aat_core.generators.core_service import optimize_core_service
from app.services.planner import build_group_plan
from app.services.project_state import default_state
from app.services.a3_export import render_a3_pdf


def test_brief_loads():
    b = load_brief()
    assert b.min_units == 200
    assert b.site["zone"] == "ACZ1"
    assert len(b.deliverables) >= 8


def test_rules_pass_default():
    report = RulesEngine().evaluate(default_state())
    assert report.score >= 70
    fails = [r for r in report.results if r.status == "fail"]
    assert len(fails) == 0


def test_massing_open_space():
    site = [[0, 0], [50, 0], [50, 56], [0, 56], [0, 0]]
    m = generate_massing(site, seed=1, storeys=8)
    assert m["metrics"]["ground_open_space_pct"] >= 45
    assert m["height_m"] > 0


def test_typical_floor_dda():
    t = generate_typical_floor(seed=3, plate_width_m=40, plate_depth_m=18)
    assert t["metrics"]["units_total"] > 0
    assert t["metrics"]["dda_count"] >= 1


def test_ground_floor_open():
    g = generate_ground_floor(seed=2)
    assert g["metrics"]["ground_open_space_pct"] >= 48


def test_core_service():
    c = optimize_core_service(unit_count=220, storeys=12)
    assert c["lifts"]["count"] >= 2
    assert c["stairs_exits"]["count"] >= 2


def test_planner_three_members():
    plan = build_group_plan(load_brief(), ["Alex", "Blair", "Casey"])
    assert len(plan["members"]) == 3
    assert plan["total_a3"] > 0
    leads = {a["lead"] for a in plan["assignments"]}
    assert leads == {"Alex", "Blair", "Casey"}


def test_a3_export(tmp_path):
    path = tmp_path / "test.pdf"
    render_a3_pdf(
        path,
        title="Test Folio",
        subtitle="Footscray",
        sheets=[
            {"title": "Sheet 1", "body": "Hello A3", "bullets": ["One", "Two"]},
            {"title": "Sheet 2", "body": "More", "bullets": []},
        ],
        members=["A", "B", "C"],
    )
    assert path.exists()
    assert path.stat().st_size > 500
