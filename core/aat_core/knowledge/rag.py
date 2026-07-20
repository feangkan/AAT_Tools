"""Simple keyword RAG over the knowledge base."""

from __future__ import annotations

from typing import Any

from .ingest import KnowledgeBase


def retrieve(query: str, limit: int = 6, kb: KnowledgeBase | None = None) -> list[dict[str, Any]]:
    base = kb or KnowledgeBase()
    if not base.chunks:
        base.load()
    hits = base.search(query, limit=limit)
    return [
        {
            "id": h.id,
            "source": h.source,
            "page": h.page,
            "folder": h.folder,
            "excerpt": h.text[:600],
        }
        for h in hits
    ]
