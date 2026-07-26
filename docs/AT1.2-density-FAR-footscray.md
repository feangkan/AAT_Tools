# AT1.2 Density & FAR — 63–67 Nicholson St, Footscray

**Verdict for the brief:** There is **no fixed FAR (plot ratio) number** for this project in the course brief, our NCC sheets, or the Maribyrnong **ACZ1** schedule. Density is controlled mainly by **preferred maximum building height** (and setbacks) for your **ACZ1 sub-precinct** — not by a Floor Area Ratio.

Use this page for **AT1.2 Planning** (not NCC).

---

## 1. What we checked (our sources)

| Source | FAR / plot ratio? | What it does say |
|--------|-------------------|------------------|
| `project-information/AAT_project_brief.pdf` | **No** | Zone **ACZ1**; plan for heights, setbacks, overshadowing, parking |
| `data/brief/project_brief.json` | **No** | Zone ACZ1; site `approx_area_sqm`: **2800** (approximate only) |
| `assessment-tasks/… AT1 Schematic Design.pdf` (AT1.2) | **No** | Evidence **maximum building heights** and **street setbacks** |
| `docs/NCC-design-catalog-footscray.md` | **No** | NCC only — FAR is not an NCC control |
| `docs/AT1.4-claude-design-handoff.md` | **No** | Structure / Class 3 focus |
| `data/rules/compliance_rules.json` | **No** | 5%/10% of GFA for services/fire — not site FAR |
| Massing generator | Optional input only | `plot_ratio` in `core/aat_core/generators/massing.py` — **you** must supply a target; nothing is pre-set |

**Conclusion from our repo:** FAR was never cleared because the brief never sets one.

---

## 2. What the planning scheme says (web — primary)

### Open these

1. **ACZ1 schedule (legal control)**  
   https://planning-schemes.app.planning.vic.gov.au/MARIBYRNONG/ordinance/37.08-s1  
   → scroll to **5. Precinct provisions** → your precinct’s **Preferred maximum building height** table.  
   → Local PDF: `resources/planning/Maribyrnong-ACZ1-Schedule-37.08-s1-Footscray-MAC.pdf`

2. **Full planning index (Clause 58, overlays, private open space)**  
   [`docs/maribyrnong-planning-resources.md`](../docs/maribyrnong-planning-resources.md)

3. **Parent ACZ clause**  
   https://planning-schemes.app.planning.vic.gov.au/Maribyrnong/ordinance/37.08

4. **Confirm which sub-precinct the site is in**  
   - VicPlan map: https://mapshare.vic.gov.au/vicplan/  
   - Search **63 Nicholson Street, Footscray** → Planning Property Report / zone layers  
   - Match the coloured precinct on the **ACZ1 precinct map** inside the schedule (images under each Precinct 1…8)

### Important finding

A full-text search of **Schedule 1 to Clause 37.08 (ACZ1)** shows **no “plot ratio” / “floor area ratio” / FAR control**.  
Built form is framed as:

- **Preferred maximum building height** (storeys + metres)  
- **Preferred setbacks** / podium–tower rules  
- Precinct guidelines (solar access, heritage, transition areas, etc.)

Example height bands in ACZ1 (depends on **sub-precinct** — confirm on map):

| Example sub-precinct | Preferred max height (from schedule text) |
|----------------------|-------------------------------------------|
| Precinct 1A / 1B | 6 storeys (19.2 m); 2–4 storey street wall |
| Precinct 1D | 10 storeys (31 m) |
| Precinct 1E | 25 storeys (76 m) |
| Precinct 6B | 6 storeys (19.2 m); 2–3 storey podium |
| Precinct 6C | 10 storeys (32 m) |
| Precinct 6D | 14 storeys (44.8 m) |

**Little Saigon / Nicholson St** sits in the Footscray MAC and is discussed against **Nicholson Street** corridors in Precinct 1 objectives; **you must confirm the exact sub-precinct on VicPlan + the precinct map** before locking a height for AT1.2.

---

## 3. Site area note (brief vs published)

| Source | Site area |
|--------|-----------|
| Our brief JSON | **~2,800 m²** (approximate polygon) |
| Public reporting on Little Saigon (news / listings) | Often **~5,110 m²** |

For studio calculations, either:
- use **brief 2,800 m²** if your tutor expects the course figure, or  
- measure the cadastral area from VicPlan / title and state which you used.

---

## 4. How to report “FAR” for design (achieved FAR)

Because the scheme does **not** give a max FAR, for your folio calculate **achieved FAR** after you set height/GFA:

\[
\textbf{Achieved FAR} = \frac{\text{Total GFA (m²)}}{\text{Site area (m²)}}
\]

### Worked sketch (brief-led, illustrative only)

Assume:
- Site = **2,800 m²** (brief)  
- Brief: ≥200 studios @ ~20 m² → ~4,000 m² residential NLA alone  
- Add circulation / core / communal / retail (often ~1.4–1.7× NLA for multi-storey student housing — use your schedules)

| If total GFA is… | Achieved FAR on 2,800 m² |
|------------------|---------------------------|
| 8,400 m² | **3.0** |
| 11,200 m² | **4.0** |
| 14,000 m² | **5.0** |
| 16,800 m² | **6.0** |

On **5,110 m²** site, the same GFA gives a **lower** FAR (e.g. 14,000 / 5,110 ≈ **2.7**).

**What to put on an A3 (AT1.2):**
1. VicPlan screenshot — zone **ACZ1** + overlays  
2. ACZ1 precinct map crop + **sub-precinct code** + preferred height table row  
3. Your massing GFA schedule  
4. One line: *“ACZ1 does not prescribe FAR; achieved FAR = X.XX based on GFA / site area.”*

---

## 5. Real-world context (secondary — not the brief)

Published Little Saigon proposals have cited forms around **8 and 12 storeys** / ~260 dwellings on ~5,110 m² (e.g. development listings). Use only as **precedent context** for AT1.2/AT1.3 — still cite **ACZ1 preferred height** for your speculative student scheme.

---

## 6. FIND IT checklist (do this in order)

1. Open VicPlan → 63–67 Nicholson St Footscray → note **ACZ1** + overlays (HO, PO, DCPO…).  
2. Open ACZ1 schedule → find your **precinct map** → read **Preferred maximum building height**.  
3. Open course brief → confirm program (200+ units, 50% ground open space).  
4. Build massing under that height → sum GFA.  
5. Compute **achieved FAR** = GFA ÷ site area.  
6. Caption sources (Chicago short form below).

---

## References (Chicago)

Department of Transport and Planning (Victoria). *Maribyrnong Planning Scheme*, Clause 37.08 Schedule 1 (Activity Centre Zone — Footscray). https://planning-schemes.app.planning.vic.gov.au/MARIBYRNONG/ordinance/37.08-s1.

Department of Transport and Planning (Victoria). VicPlan. https://mapshare.vic.gov.au/vicplan/.

RMIT University. *Architecture Advanced Technology Project Outline & Brief*. ARCH3372/2650. `project-information/AAT_project_brief.pdf`.

RMIT University. *Assessment Task 1: Schematic Design* (AT1.2 Planning Report). `assessment-tasks/Assessment Task 1_ Schematic Design.pdf`.

---

*AT1.2 density note · no statutory FAR in ACZ1 · use preferred height + achieved FAR*
