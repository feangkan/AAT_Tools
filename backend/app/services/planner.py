"""Group planner — split deliverables across 3 members."""

from __future__ import annotations

from typing import Any

from aat_core.brief.registry import BriefRegistry


ROLE_BIAS = {
    0: ["AT1.1", "AT1.2", "AT2.1", "AT3.1"],  # site / planning / NCC / systems
    1: ["AT1.3", "AT1.4", "AT1.5", "AT3.2"],  # precedents / structure / facade / lighting
    2: ["AT1.6", "AT2.2", "AT3.3"],  # drawings / DD / portfolio lead
}


def build_group_plan(brief: BriefRegistry, members: list[str]) -> dict[str, Any]:
    members = (members + ["Member A", "Member B", "Member C"])[:3]
    deliverables = brief.deliverables
    assignments: list[dict[str, Any]] = []

    # Round-robin with role bias
    claim_counts = {m: 0 for m in members}
    a3_counts = {m: 0 for m in members}

    for d in deliverables:
        preferred = None
        for idx, ids in ROLE_BIAS.items():
            if d.id in ids:
                preferred = members[idx]
                break
        if preferred is None:
            preferred = min(members, key=lambda m: (claim_counts[m], a3_counts[m]))
        # Support: one secondary reviewer
        support = min(
            (m for m in members if m != preferred),
            key=lambda m: claim_counts[m],
            default=None,
        )
        claim_counts[preferred] += 1
        a3_counts[preferred] += d.min_a3_pages
        assignments.append(
            {
                "id": d.id,
                "name": d.name,
                "week": d.week,
                "task": d.task,
                "min_a3_pages": d.min_a3_pages,
                "format": d.format,
                "lead": preferred,
                "support": support,
                "status": "todo",
                "presentation_minutes": d.presentation_minutes,
            }
        )

    by_member = {
        m: [a for a in assignments if a["lead"] == m] for m in members
    }
    weeks = sorted({a["week"] for a in assignments})
    timeline = []
    for w in weeks:
        timeline.append(
            {
                "week": w,
                "items": [a for a in assignments if a["week"] == w],
            }
        )

    return {
        "members": members,
        "assignments": assignments,
        "by_member": by_member,
        "timeline": timeline,
        "workload": {
            m: {
                "tasks": claim_counts[m],
                "a3_pages": a3_counts[m],
            }
            for m in members
        },
        "total_a3": sum(d.min_a3_pages for d in deliverables),
        "notes": [
            "Equal presentation participation required (10 min max per review).",
            "Lead owns A3 content; support peer-reviews against Inspector checklist.",
            "Export this plan as an A3 sheet for the group folio.",
        ],
    }
