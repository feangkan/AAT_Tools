"""FastAPI application for AAT Studio Tools."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "core"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import routes

app = FastAPI(
    title="AAT Studio Tools",
    description="Studio cockpit for RMIT ARCH3372 Footscray student accommodation",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api")

# Serve knowledge previews if present
kb_prev = ROOT / "data" / "knowledge" / "previews"
if kb_prev.exists():
    app.mount("/previews", StaticFiles(directory=str(kb_prev)), name="previews")


@app.get("/health")
def health():
    return {"status": "ok", "service": "aat-studio-tools"}
