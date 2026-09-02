# AT2 continues AT1 — Week 5/6 working notes

**Project:** 63–67 Nicholson St, Footscray · ARCH3372  
**Rule:** AT2 is design development of the same building AT1 already argued. Hybrid B and Class 3 lodging are not reopened. The **structural bay** was corrected in Week 6 — see below.

**Presentation content — use these files.** Course minimums are met; the extra slides are included in the set you present.

| Report | File | Slides | Course min |
|---|---|---|---|
| AT2.1 NCC | [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) | **12** | 6 × A3 |
| AT2.2 LHD + BADS | [`docs/AT2.2-lhd-bads-report.md`](./AT2.2-lhd-bads-report.md) | **16** | 9 × A3 |
| AT2.3 Energy | [`docs/AT2.3-environmental-report.md`](./AT2.3-environmental-report.md) | **12** | 6 × A3 |
| First Nations sourcing (structure strategy) | [`docs/AT2-first-nations-sourcing.md`](./AT2-first-nations-sourcing.md) | **2** | — (course-wide requirement, not a numbered AT2.x) |
| Facade strategy (modular TMT panel) | [`docs/AT2-facade-panel-strategy.md`](./AT2-facade-panel-strategy.md) | **2** | — |
| Mass timber fire resistance | [`docs/AT2-fire-resistance.md`](./AT2-fire-resistance.md) | **2** | — |

Each section is one slide: real clause text, **bold** keywords, analysis on *this* building, a table, a short citation. Not AI-prompt language.

---

## Week 6 correction: real bay is 3.6 × 7.2 m, not 6.0 m

AT2.2 and AT2.3 were originally written before a dimensioned drawing set existed, on an assumed uniform 6.0 m grid. The Week 6 Revit model (`Nicholson St_17.rvt`, plotted as `Week 6 Drawing.pdf`) fixes the real geometry:

- **Facade/coordination module: 3.6 m.** Every studio (Unit Typology A, A501) is one 3.6 m-wide bay.
- **Structural column grid: 3.6 m × 7.2 m rectangular bay** (A400). Glulam beams span **7.2 m** column-to-column; CLT floor panels span one-way across the **3.6 m** direction between beams.
- **Real named products** (A400): CLT floor = NeXTimber NX5-150 (5-ply); glulam beam = NeXTimber GL13, 135 × 630 mm; glulam column = ASH MASSLAM SL33, 265 × 260 mm; connections = threaded rod + steel plate epoxied into the glulam end grain (A401), not the generic "concealed steel connector" language in the AT1.4 draft.
- **Building height:** the site carries two sub-precinct envelopes (Schedule 1B 19.2 m/6 storeys at the street frontage; Schedule 1D 31 m/10 storeys with a 5 m setback above 5 storeys, A200) — the modelled building runs to **31.0 m / 9 residential levels + roof**, not a flat "6 storeys/19.2 m" assumption.

**AT2.2 and AT2.3 have been corrected** against this real bay — see each file's opening "Correction against the Week 6 Revit model" note. Two real compliance risks surfaced by the correction, not previously visible on the wrong 6.0 m assumption:

- **D27 room depth** — the real 7.2 m studio depth *exceeds* the 6.75 m limit (2.5 × 2.7 m FTC). Flagged in AT2.2 §7/§13 with two honest fixes; not yet resolved in a drawing.
- **D20 balcony area** — a straight 1.8 m-deep balcony on the real 3.6 m bay is only 6.48 m², short of the 8 m² minimum; needs ~2.25 m depth. Flagged in AT2.2 §4/§13 and AT2.3 §12 (bigger cantilever, bigger thermal bridge to detail).

Both are carried forward as **open AT2.4 drawing questions**, not silently assumed away.

**Claude Design (A3 PDFs):** paste the three prompts in [`docs/AT2-claude-design-handoff.md`](./AT2-claude-design-handoff.md) at https://claude.ai/design with repo branch `cursor/at2-week5-f836` connected. That handoff is a production tool — do not put it in the tutor folio.

---

## Corrections made against the actual current NCC text

Checking the repo's 2015-edition PDFs and the live NCC 2022 site turned up a few figures that needed fixing from what earlier drafts assumed:

| Topic | Was assumed | Actual (NCC 2022, checked against ABCB site) |
|---|---|---|
| Class 3 travel distance | "≤40 m" | **6 m** (unit door to point of exit choice) / **20 m** (corridor to exit). 40 m applies to Class 5–9, not Class 2/3 |
| Exit separation | not stated | **9–45 m** apart for a Class 3 building (D2D6) |
| Sprinkler trigger | "2+ storeys" | **Rise in storeys ≥ 4** and effective height ≤ 25 m (E1D6) |
| Wet-area pathway | "Part 10.2" | **F2D2 + Specification 26** — Part 10.2 sits in the Housing Provisions, which only cover Class 1/10 (houses), not our Class 3 building |
| Energy pathway | H6 + J1P2/J3 as if Class 2 | **J1P1 + J4 + J6** for Class 3 in climate zone 6. H6 is Class 1/10; J1P2/J1P3/J3 are Class 2 SOU |

`data/rules/compliance_rules.json` and `core/aat_core/generators/core_service.py` still use the old 40 m figure for the automated compliance checks and travel-distance estimator — that is a separate code fix, not done here.

---

## AT1 → AT2 carry-forward (locked)

| AT1 piece | What was decided | AT2 uses it for |
|---|---|---|
| AT1.1 Site | Wurundjeri Country, solar, entry, 50% ground open space | Ground plan, accessible path from street |
| AT1.2 Planning | ACZ1; no FAR — height by sub-precinct; Parking Overlay; Clause 58 | AT2.2 D18–D21 and D26–D29 |
| AT1.3 Precedents | Fed AT1.4's structural precedent set | Cited only where a clause needs a built example |
| AT1.4 Structure | Hybrid B; **3.6 × 7.2 m bay** (corrected Week 6, was 6.0 m); dual stairs inside the RC core; ~20 rooms/floor | AT2.1 escape/structure; AT2.2 room depth; AT2.3 envelope |
| AT1.4 NCC | Class 3 lodging (A6G4) + Class 6 retail (A6G1) | All three AT2 reports. G7/J3 applied as overlay or comparison, not a reclass |
| AT1.6 Schematic drawings | Typical floor that AT2.4 will develop | Travel, depth and WFR figures are current set-out, to be confirmed in Revit |

---

## Canvas numbering

| ID | Name | Week | Min | This folio |
|---|---|---|---|---|
| AT2.1 | NCC Report | 5 | 6 × A3 | **12** slides |
| AT2.3 | Environmental / energy | 5 | 6 × A3 | **12** slides |
| AT2.2 | LHD + BADS | 6 | 9 × A3 | **16** slides |
| AT2.4 | DD drawings (Revit) | 4–7 | drawing set | Week 6 model exists (`Week 6 Drawing.pdf`, 24 sheets) — see below |

**Submission dates (per the Week 6 course announcement — supersedes the "Mon 7 Sep" AT2-only date used in earlier drafts of this brief):** classes resume Mon 7 Sep (Week 7); **AT1 + AT2 bound into one PDF, submitted to Canvas by 5pm Fri 11 Sep**; Week 7 tutorial is the Mid-Semester Review, presenting the submitted work with a particular focus on the AT2 drawing set.

---

## Ready-for-submission checklist (Week 6)

| Item | Status |
|---|---|
| AT2.1 NCC, AT2.3 Energy (Week 5), AT2.2 LHD/BADS (Week 6) | Written; bay/grid corrected against the real Week 6 model |
| First Nations sourcing slides | Written (`AT2-first-nations-sourcing.md`) — answers the course's percentage-sourced and structural-grid-as-Country questions directly |
| Facade strategy (TMT panel) | Written (`AT2-facade-panel-strategy.md`) — resolves the unfinished note on sheet A402 |
| Mass timber fire resistance | Written (`AT2-fire-resistance.md`) — structure (char-design on real member sizes) + facade cavity interface |
| NCC resource (buildingtools.co) | Added to `resources/README.md`, both cursor branches |
| AT2.4 drawing set | Exists as `Week 6 Drawing.pdf` (A000–A506, A700 — 24 sheets): plans, elevations, sections, construction/facade/typical details, means-of-escape, unit schedule, shadow studies, renders, building performance. **Unit areas are not yet tagged** in the Revit schedule (A501 shows "Not Placed") — confirm before the bound PDF goes in |
| D27 depth risk (real 7.2 m studio depth vs 6.75 m limit) | **Open** — flagged in AT2.2 §7/§13, not yet resolved in a drawing |
| D20 balcony depth risk (6.48 m² at 1.8 m vs 8 m² min on the real 3.6 m bay) | **Open** — flagged in AT2.2 §4/§13 and AT2.3 §12 |

---

## Still open

**Q1 — Typical floor:** ~~escape, D27 depth and 10% WFR are stated against the 6.0 m grid set-out, not a dimensioned Revit plan~~ — **resolved**: the Week 6 model gives the real 3.6 × 7.2 m bay (see correction above). D27 depth and D20 balcony now read as real, unresolved compliance risks rather than an unconfirmed assumption.

**Q2 — Numbers to confirm:** ~~storeys (Precinct 1B default is 6 / 19.2 m)~~ — **resolved**: the site carries two sub-precinct envelopes (1B 19.2 m/6-storey street frontage, 1D 31 m/10-storey with setback); the model builds to 31.0 m / 9 levels + roof. Basement: **yes** — B1 exists (FFL 14.740). Car parking: ground/basement plan prioritises bike store + loading bay; confirm any visitor/accessible car bays against AS 2890.1/.6.

**Q3 — Group:** Ryan Tan Yip Kai (S3919685), Danna Diaz (S4073826), Kankawee Maksomboon (S4097770) — per the Week 6 research pack cover sheet. Tutor last name still needed for the file naming convention.

---

*ARCH3372 · AT2 is design development of AT1 · 63–67 Nicholson St*
