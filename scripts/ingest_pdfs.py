#!/usr/bin/env python3
"""Ingest all PDFs into the knowledge base."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))

from aat_core.knowledge.ingest import ingest_pdfs


def main():
    kb = ingest_pdfs()
    print(f"Ingested {len(kb.chunks)} chunks → {kb.index_path}")


if __name__ == "__main__":
    main()
