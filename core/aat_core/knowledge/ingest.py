"""PDF ingest → searchable knowledge base (handles CID-encoded PDFs via image render)."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
KB_DIR = ROOT / "data" / "knowledge"
PDF_FOLDERS = [
    ROOT / "project-information",
    ROOT / "assessment-tasks",
    ROOT / "resources",
]


@dataclass
class Chunk:
    id: str
    source: str
    page: int
    text: str
    folder: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class KnowledgeBase:
    def __init__(self, index_path: Path | None = None):
        self.index_path = index_path or (KB_DIR / "index.json")
        self.chunks: list[Chunk] = []
        if self.index_path.exists():
            self.load()

    def load(self) -> None:
        with open(self.index_path, encoding="utf-8") as f:
            data = json.load(f)
        self.chunks = [Chunk(**c) for c in data.get("chunks", [])]

    def save(self) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(
                {"chunks": [c.to_dict() for c in self.chunks], "count": len(self.chunks)},
                f,
                indent=2,
            )

    def search(self, query: str, limit: int = 8) -> list[Chunk]:
        tokens = [t.lower() for t in re.findall(r"[a-zA-Z0-9]+", query) if len(t) > 2]
        if not tokens:
            return self.chunks[:limit]
        scored: list[tuple[int, Chunk]] = []
        for chunk in self.chunks:
            text = chunk.text.lower()
            score = sum(text.count(t) for t in tokens)
            if score:
                scored.append((score, chunk))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored[:limit]]


def _extract_text_page(page) -> str:
    """Best-effort text extraction; CID fonts may yield little."""
    try:
        text = page.get_text("text") or ""
    except Exception:
        text = ""
    # Filter out mostly-null / control garbage
    printable = "".join(ch for ch in text if ch.isprintable() or ch in "\n\t ")
    letters = sum(1 for ch in printable if ch.isalpha())
    if letters < 40:
        return ""
    return printable.strip()


def _page_meta_fallback(doc_name: str, page_index: int, folder: str) -> str:
    """When OCR/text fails, store a useful placeholder for retrieval by filename."""
    return (
        f"[PDF page image] {doc_name} page {page_index + 1} "
        f"from {folder}. Content is image-based / CID-encoded; "
        f"refer to original PDF for full text. Keywords: "
        f"{doc_name.replace('_', ' ').replace('-', ' ')} "
        f"AAT architecture assessment Footscray student accommodation NCC BADS."
    )


def ingest_pdfs(
    folders: list[Path] | None = None,
    out_dir: Path | None = None,
    render_preview: bool = True,
) -> KnowledgeBase:
    import fitz  # pymupdf

    folders = folders or PDF_FOLDERS
    out_dir = out_dir or KB_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    preview_dir = out_dir / "previews"
    if render_preview:
        preview_dir.mkdir(parents=True, exist_ok=True)

    kb = KnowledgeBase(out_dir / "index.json")
    chunks: list[Chunk] = []
    catalog: list[dict[str, Any]] = []

    for folder in folders:
        if not folder.exists():
            continue
        for pdf in sorted(folder.rglob("*.pdf")):
            try:
                doc = fitz.open(pdf)
            except Exception as exc:
                catalog.append({"file": pdf.name, "error": str(exc)})
                continue
            page_count = doc.page_count
            extracted_pages = 0
            for i, page in enumerate(doc):
                text = _extract_text_page(page)
                if not text:
                    text = _page_meta_fallback(pdf.stem, i, folder.name)
                else:
                    extracted_pages += 1
                chunk_id = f"{folder.name}/{pdf.stem}/p{i+1}"
                chunks.append(
                    Chunk(
                        id=chunk_id,
                        source=str(pdf.relative_to(ROOT)),
                        page=i + 1,
                        text=text[:8000],
                        folder=folder.name,
                    )
                )
                if render_preview and i < 2:
                    try:
                        pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2))
                        pix.save(str(preview_dir / f"{pdf.stem}_p{i+1}.png"))
                    except Exception:
                        pass
            catalog.append(
                {
                    "file": str(pdf.relative_to(ROOT)),
                    "pages": page_count,
                    "text_pages": extracted_pages,
                    "cid_heavy": extracted_pages == 0,
                }
            )
            doc.close()

    # Seed curated excerpts so RAG works even when PDFs are CID-locked
    curated = out_dir / "curated_excerpts.json"
    if curated.exists():
        with open(curated, encoding="utf-8") as f:
            for item in json.load(f):
                chunks.append(Chunk(**item))

    kb.chunks = chunks
    kb.save()
    with open(out_dir / "catalog.json", "w", encoding="utf-8") as f:
        json.dump({"documents": catalog, "chunk_count": len(chunks)}, f, indent=2)
    return kb
