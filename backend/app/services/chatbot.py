"""Provider-agnostic chatbot with offline RAG fallback."""

from __future__ import annotations

from typing import Any

import httpx

from aat_core.knowledge.rag import retrieve
from aat_core.brief.registry import load_brief


SYSTEM_CONTEXT = """You are AAT Studio Assistant for an RMIT ARCH3372 group project:
student accommodation + retail at 63-67 Nicholson St, Footscray (ACZ1), on Wurundjeri Country.
Help with brief requirements, NCC/BADS/LHD compliance, planning, massing, plans, and A3 presentations.
Always cite Australian sources when possible (Vicmap, NCC CC BY 4.0, Clause 58).
Keep answers concise and actionable for a 3-person student team.
"""


def chat(
    message: str,
    *,
    provider: str = "offline",
    api_key: str | None = None,
    model: str | None = None,
) -> dict[str, Any]:
    hits = retrieve(message, limit=5)
    brief = load_brief().summary()
    context_blocks = [
        f"Project: {brief}",
        "Retrieved knowledge:",
        *[f"- ({h['source']} p{h['page']}) {h['excerpt'][:280]}" for h in hits],
    ]
    context = "\n".join(context_blocks)

    if provider == "offline" or not api_key:
        answer = _offline_answer(message, hits, brief)
        return {
            "provider": "offline",
            "answer": answer,
            "sources": hits,
            "presentation_bullets": _presentation_bullets(message, hits),
        }

    try:
        if provider in ("openai", "azure"):
            answer = _openai_chat(message, context, api_key, model or "gpt-4o-mini", provider)
        elif provider == "anthropic":
            answer = _anthropic_chat(message, context, api_key, model or "claude-sonnet-4-20250514")
        elif provider == "ollama":
            answer = _ollama_chat(message, context, model or "llama3.2")
        else:
            answer = _offline_answer(message, hits, brief)
            provider = "offline"
    except Exception as exc:
        answer = (
            _offline_answer(message, hits, brief)
            + f"\n\n_(LLM provider error: {exc}; fell back to offline.)_"
        )
        provider = "offline-fallback"

    return {
        "provider": provider,
        "answer": answer,
        "sources": hits,
        "presentation_bullets": _presentation_bullets(message, hits),
    }


def _offline_answer(message: str, hits: list[dict], brief: dict) -> str:
    q = message.lower()
    parts = [
        f"**Project snapshot:** {brief.get('name')} @ {brief.get('site')} "
        f"(zone {brief.get('zone')}, ≥{brief.get('min_units')} units, "
        f"{brief.get('open_space_pct')}% ground open space).",
    ]
    if "unit" in q or "studio" in q or "dda" in q:
        parts.append(
            "**Accommodation:** ≥200 studios (15–25 sqm), DDA rooms 30–35 sqm at **1 per 20 units per floor**, "
            "FTC ≥2.7 m, BADS/Clause 58 + LHD."
        )
    if "ncc" in q or "egress" in q or "fire" in q or "exit" in q:
        parts.append(
            "**NCC focus:** AT1.4 lock — Class 3 lodging + Class 6 retail; D1 exits (min 2) & travel ≤40 m; F2 sanitary; Section J energy; "
            "AS1428.1 access; AS2890.1 parking."
        )
    if "plan" in q or "setback" in q or "height" in q or "acz" in q:
        parts.append(
            "**Planning:** ACZ1 Footscray; overlays DCPO/HO/PO; check street setbacks, height, overshadowing, "
            "overlooking, carparking. Justify variations in portfolio."
        )
    if "a3" in q or "present" in q or "folio" in q:
        parts.append(
            "**Deliverables:** All reports are **A3 landscape folios** (AT1.1/1.2 ≥9 pages, AT2.1 NCC ≥6, AT2.2 LHD/BADS ≥9, AT2.3 energy ≥6, AT2.4 Revit DD set). "
            "Use Export → A3 in the studio cockpit."
        )
    if "country" in q or "indigenous" in q or "plant" in q or "landscape" in q:
        parts.append(
            "**Country / landscape:** Design with Wurundjeri Country; use indigenous species "
            "(River Red Gum, Kangaroo Grass, Lomandra, Dianella, Acacia, Allocasuarina) in ≥50% ground open space."
        )
    if hits:
        parts.append("**From knowledge base:**")
        for h in hits[:3]:
            parts.append(f"- {h['source']} p{h['page']}: {h['excerpt'][:180]}…")
    parts.append(
        "_Offline mode — add an API key (OpenAI / Anthropic / Ollama) for generative answers._"
    )
    return "\n\n".join(parts)


def _presentation_bullets(message: str, hits: list[dict]) -> list[str]:
    bullets = [
        "Site: 63–67 Nicholson St, Footscray — ACZ1 on Wurundjeri Country",
        "Program: 200+ student studios + retail + communal + 50% ground open space",
        "Compliance loop: Brief → VicPlan → NCC/BADS/LHD → revise",
    ]
    for h in hits[:2]:
        bullets.append(f"Ref: {h['source']} p{h['page']}")
    return bullets


def _openai_chat(message: str, context: str, api_key: str, model: str, provider: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    if provider == "azure":
        # Expect api_key as full endpoint|key for simplicity is too magic; use OpenAI-compatible
        pass
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_CONTEXT + "\n\n" + context},
            {"role": "user", "content": message},
        ],
        "temperature": 0.3,
    }
    with httpx.Client(timeout=60) as client:
        r = client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]


def _anthropic_chat(message: str, context: str, api_key: str, model: str) -> str:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": 1200,
        "system": SYSTEM_CONTEXT + "\n\n" + context,
        "messages": [{"role": "user", "content": message}],
    }
    with httpx.Client(timeout=60) as client:
        r = client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def _ollama_chat(message: str, context: str, model: str) -> str:
    url = "http://127.0.0.1:11434/api/chat"
    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": SYSTEM_CONTEXT + "\n\n" + context},
            {"role": "user", "content": message},
        ],
    }
    with httpx.Client(timeout=120) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        return r.json()["message"]["content"]
