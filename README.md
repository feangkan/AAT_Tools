# AAT Studio Tools

Studio cockpit for **RMIT ARCH3372 / Architecture Advanced Technology (2650)** — speculative multi-storey **student accommodation + retail** at **63–67 Nicholson Street, Footscray** (ACZ1, Wurundjeri Country).

Two surfaces over one shared Python core:

| Surface | Purpose |
|---------|---------|
| **Web app** (`frontend/` + `backend/`) | Group planner, Inspector compliance loop, Vicmap/solar, massing & plan generators, chatbot, A3 export |
| **pyRevit extension** (`pyrevit/`) | Build massing, import floor JSON, make A3 sheets, export schedules (run on Windows/Revit) |

All assessment deliverables target **A3 landscape** folios.

## Quick start

```bash
# 1. Python deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Ingest PDFs into knowledge base
python scripts/ingest_pdfs.py

# 3. API
chmod +x scripts/*.sh
./scripts/run_backend.sh
# → http://127.0.0.1:8000/docs

# 4. Web UI (new terminal)
cd frontend && npm install && cd ..
./scripts/run_frontend.sh
# → http://127.0.0.1:5173
```

Smoke test:

```bash
source .venv/bin/activate
python scripts/smoke_test.py
pytest -q
```

## Repo layout

```
core/aat_core/     Shared brief, rules, Vicmap/OSM, solar, generators, RAG
backend/           FastAPI studio API
frontend/          React + Vite + Tailwind cockpit
pyrevit/           pyRevit extension (author here, run in Revit)
data/brief/        Machine-readable project brief + indigenous palette
data/rules/        NCC / BADS / LHD / AS rule packs
data/knowledge/    Curated excerpts + ingested PDF index
project-information/ assessment-tasks/ resources/   Your uploaded PDFs
```

## Australian open data (free & attributed)

- **Vicmap Planning** ArcGIS REST — zones/overlays (CC BY 4.0)
- **NCC 2022 XML** on data.gov.au (CC BY 4.0)
- **Clause 58 / Better Apartments** — planning.vic.gov.au
- **OpenStreetMap** — surrounding footprints (ODbL)
- Indigenous palette sourced conceptually from VicFlora / council urban forest open data

## Modules

1. **Group planner** — split AT1.1–AT3.x across 3 members + A3 export  
2. **Inspector** — brief / planning / NCC / BADS / LHD loop with suggestions  
3. **Site & solar** — Vicmap pack + 2.5D winter solstice shadows  
4. **Generators** — massing (seed), typical & ground plans (difference rule, hierarchy), core/lifts/egress  
5. **Chat / presentation agent** — offline RAG or BYOK (OpenAI / Anthropic / Ollama) → A3 layout  
6. **Country** — Wurundjeri acknowledgement + indigenous planting for ≥50% open space  
7. **Details** — structure / facade bays / AT1.3 precedent slots  
8. **pyRevit** — massing DirectShapes, floor JSON detail lines, A3 sheets, CSV export  

## Revit setup

1. Install [pyRevit](https://github.com/pyrevitlabs/pyRevit)  
2. Add `pyrevit/AAT_Tools.extension` to your pyRevit extensions folder  
3. Reload pyRevit  
4. Save generator JSON from the web app to `~/Documents/aat_tools/massing.json` and `typical_floor.json`  

## Note on PDFs

Many course PDFs use CID fonts without Unicode maps. Ingest stores page metadata + **curated excerpts** in `data/knowledge/curated_excerpts.json` so search/chat still work. Previews of the first pages are rendered when possible.
