# AT2 continues AT1 — Week 5 working notes

**Project:** 63–67 Nicholson St, Footscray · ARCH3372  
**Rule:** AT2 is design development of the same building AT1 already argued. Hybrid B, the 6.0 m grid, and Class 3 lodging are not reopened.

**The presentation content is here:** [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) — 8 sections, ready to read from or paste into slides. Real NCC 2022 clause text, bolded keywords, tables. This is the file to use.

Week 6: [`docs/AT2.2-lhd-bads-handoff.md`](./AT2.2-lhd-bads-handoff.md) — LHD & BADS starter.

---

## Corrections made against the actual current NCC text

Checking the repo's 2015-edition PDFs and the live NCC 2022 site turned up a few figures that needed fixing from what earlier drafts assumed:

| Topic | Was assumed | Actual (NCC 2022, checked against ABCB site) |
|---|---|---|
| Class 3 travel distance | "≤40 m" | **6 m** (unit door to point of exit choice) / **20 m** (corridor to exit). 40 m applies to Class 5–9, not Class 2/3 |
| Exit separation | not stated | **9–45 m** apart for a Class 3 building (D2D6) |
| Sprinkler trigger | "2+ storeys" | **Rise in storeys ≥ 4** and effective height ≤ 25 m (E1D6) |
| Wet-area pathway | "Part 10.2" | **F2D2 + Specification 26** — Part 10.2 sits in the Housing Provisions, which only cover Class 1/10 (houses), not our Class 3 building |

`data/rules/compliance_rules.json` and `core/aat_core/generators/core_service.py` still use the old 40 m figure for the automated compliance checks and travel-distance estimator — that is a separate code fix, not done here, since it touches the generator logic and test suite. Flag if you want that corrected too.

---

## AT1 → AT2 carry-forward (locked)

| AT1 piece | What was decided | AT2 uses it for |
|---|---|---|
| AT1.1 Site | Wurundjeri Country, solar, entry, 50% ground open space | Ground plan, accessible path from street |
| AT1.2 Planning | ACZ1; no FAR — height by sub-precinct; Parking Overlay | AS 2890.1 section references the overlay |
| AT1.3 Precedents | Fed AT1.4's structural precedent set | Not repeated in AT2.1 — cited only where a clause needs a built example |
| AT1.4 Structure | Hybrid B; 6.0 m grid; dual stairs inside the RC core; ~20 rooms/floor | AT2.1 §4 (structure) and §2 (escape) build directly on this |
| AT1.4 NCC | Class 3 lodging (A6G4) + Class 6 retail (A6G1) | AT2.1 §1 repeats and sources this properly against the current NCC text |
| AT1.6 Schematic drawings | Typical floor that AT2.4 will develop | AT2.1 §2 travel figures are stated as based on the current set-out, to be confirmed once Revit is dimensioned |

---

## Canvas numbering

| ID | Name | Week | Min |
|---|---|---|---|
| AT2.1 | NCC Report | 5 | 6 × A3 |
| AT2.3 | Environmental / energy | 5 | 6 × A3 |
| AT2.2 | LHD + BADS | 6 | 9 × A3 |
| AT2.4 | DD drawings (Revit) | 4–7 | drawing set |

AT2 package due Mon 7 Sep 12:00.

---

## Still open

**Q1 — Scope:** AT2.1 only this week, or also start AT2.3 (energy), which the syllabus also lists for Week 5?

**Q2 — Typical floor:** the escape section states its travel/separation figures against the 6.0 m grid set-out, not a dimensioned Revit plan. Send the actual typical-floor drawing when it exists so those numbers can be swapped for real dimensions.

**Q3 — Numbers to confirm:** storeys (Precinct 1B default is 6 / 19.2 m), basement yes/no, any car parking beyond bikes/loading.

**Q4 — Group:** three names, AT2.1 lead, tutor last name (for the file naming convention).

---

*ARCH3372 · AT2 is design development of AT1 · 63–67 Nicholson St*
