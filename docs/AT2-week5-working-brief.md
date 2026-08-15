# AT2 continues AT1 — Week 5 working notes

**Project:** 63–67 Nicholson St, Footscray · ARCH3372  
**Rule:** AT2 is design development of the same building AT1 already argued. Hybrid B, the 6.0 m grid, and Class 3 lodging are not reopened.

**Presentation content — use these files.** Course minimums are met; the extra slides are included in the set you present.

| Report | File | Slides | Course min |
|---|---|---|---|
| AT2.1 NCC | [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) | **12** | 6 × A3 |
| AT2.2 LHD + BADS | [`docs/AT2.2-lhd-bads-report.md`](./AT2.2-lhd-bads-report.md) | **16** | 9 × A3 |
| AT2.3 Energy | [`docs/AT2.3-environmental-report.md`](./AT2.3-environmental-report.md) | **12** | 6 × A3 |

Each section is one slide: real clause text, **bold** keywords, analysis on *this* building, a table, a short citation. Not AI-prompt language.

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
| AT1.4 Structure | Hybrid B; 6.0 m grid; dual stairs inside the RC core; ~20 rooms/floor | AT2.1 escape/structure; AT2.2 room depth; AT2.3 envelope |
| AT1.4 NCC | Class 3 lodging (A6G4) + Class 6 retail (A6G1) | All three AT2 reports. G7/J3 applied as overlay or comparison, not a reclass |
| AT1.6 Schematic drawings | Typical floor that AT2.4 will develop | Travel, depth and WFR figures are current set-out, to be confirmed in Revit |

---

## Canvas numbering

| ID | Name | Week | Min | This folio |
|---|---|---|---|---|
| AT2.1 | NCC Report | 5 | 6 × A3 | **12** slides |
| AT2.3 | Environmental / energy | 5 | 6 × A3 | **12** slides |
| AT2.2 | LHD + BADS | 6 | 9 × A3 | **16** slides |
| AT2.4 | DD drawings (Revit) | 4–7 | drawing set | not this week |

AT2 package due Mon 7 Sep 12:00.

---

## Still open

**Q1 — Typical floor:** escape, D27 depth and 10% WFR are stated against the 6.0 m grid set-out, not a dimensioned Revit plan. Swap in real dimensions when the typical-floor drawing exists.

**Q2 — Numbers to confirm:** storeys (Precinct 1B default is 6 / 19.2 m), basement yes/no, any car parking beyond bikes/loading.

**Q3 — Group:** three names, AT2.1 / AT2.2 / AT2.3 leads, tutor last name (for the file naming convention).

---

*ARCH3372 · AT2 is design development of AT1 · 63–67 Nicholson St*
