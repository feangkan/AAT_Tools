# AT2 — Mass Timber Fire Resistance

**63–67 Nicholson Street, Footscray · ACZ1 · Wurundjeri Country**
**Class 3 residential over Class 6 retail · NeXTimber CLT/glulam on ASH MASSLAM columns, 3.6 × 7.2 m bay**

*How to use this document:* two slides — structural char-design first, then the facade/cavity fire interface the new TMT panel strategy introduces. Written against the real named members on sheet A400, not generic "timber" sizing.

---

## 1. Structural fire resistance: char-design on the real member sizes

> **B1P1 — Structural reliability.** A building or structure must perform adequately under all reasonably expected design actions and withstand extreme or frequently repeated design actions, including sustaining local damage without disproportionate collapse.
>
> **E1D6 — Sprinklers.** Required throughout a Class 2 or 3 building where the rise in storeys is **4 or more** and the effective height is not more than 25 m.
>
> — ABCB, *NCC 2022*, Volume One, cl. B1P1, E1D6.

Because CLT and glulam are combustible, B1P1's fire-scenario response is **char-design**: sizing a sacrificial outer layer into the member so the *residual* cross-section still carries the design load for the required Fire-Resistance Level (FRL), rather than protecting the timber with fire-rated linings (encapsulation). Softwood glulam and CLT char at roughly **0.65–0.7 mm/minute** on an exposed face; the required FRL sets how many minutes of that sacrificial layer to add.

This building triggers **E1D6 sprinklers**: the elevation (A200) shows **9 storeys above ground + roof** (FFL 17.740 to 48.740, 31.0 m) — well past the "4 or more storeys" trigger, sprinkler-protected throughout per AS 2118.1. A sprinklered Class 3 building typically needs a **60-minute FRL** on primary structure (confirm against the fire engineer's report before AT2.4) rather than the 90-minute figure an unsprinklered building of this height would need.

Applying a 60-minute char allowance (~0.7 mm/min × 60 min ≈ **42 mm** char depth per exposed face, plus a zero-strength buffer layer per AS 1720.4) to the real member sizes on A400:

| Member | Real size (A400) | Exposed faces | Char loss (60 min, ~42 mm/face) | Residual section |
|---|---|---|---|---|
| Glulam column — ASH MASSLAM SL33 | 265 × 260 mm | 4 faces (freestanding) | ~42 mm each face | ~181 × 176 mm — check against reduced axial load |
| Glulam beam — NeXTimber GL13 | 135 × 630 mm | 3 faces (soffit + 2 sides; top is under the floor) | ~42 mm each exposed face | ~51 × 588 mm — width is now the governing dimension |
| CLT floor panel — NeXTimber NX5-150 (5-ply) | Not dimensioned on A400 (panel thickness not tagged) | 1 face (soffit, if exposed) | ~42 mm from the exposed face | Confirm remaining plies still carry the floor load — flag for the structural engineer |

**The real finding:** the 135 mm-wide glulam beam is the tightest member — a 42 mm char loss on each side of a 135 mm width removes nearly a third of its net width before the zero-strength layer is even accounted for. This is worth carrying to AT2.4 as an open structural question (confirm with a fire engineer whether BM-01 needs encapsulation on its narrow faces instead of full exposure), rather than assuming every exposed member automatically works at "structure as finish."

| Fire strategy | Where it applies |
|---|---|
| Char-design, full exposure | Columns (265 × 260, largest cross-section) |
| Char-design, check narrow face | Beams (135 mm width — flag for engineer) |
| Encapsulation (if char fails) | Narrow beam faces only, keeping the soffit exposed |
| Sprinklers throughout | Triggered by 9 storeys / 31 m (E1D6) |

---

## 2. Where the facade panel and fire resistance meet

The modular Thermally Modified Timber facade (see `AT2-facade-panel-strategy.md`) sits directly in front of the CLT wall panel it is meant to protect from weather — which means its own fire performance now has to coordinate with the structure behind it, not be assumed separately.

**TMT's fire classification is the weakest of the five panel systems compared** (Class B/C, improving to B-s1,d0 with fire treatment) against terracotta or GFRC's Class A1 non-combustible rating. On a sprinklered Class 3 building this is manageable, but only with the same cavity discipline a non-combustible rainscreen would need anyway:

- **Cavity fire barriers at every floor line.** The 25–40 mm ventilated cavity behind the TMT panel is a continuous vertical path unless interrupted — an intumescent horizontal barrier at each floor line (open under normal conditions for drainage/ventilation, swelling shut under heat) stops fire running floor-to-floor inside the cavity, independent of whether the panel face itself is combustible.
- **Fire-treated TMT at lower floors / near openings.** Reserve the fire-treated B-s1,d0 grade for the podium and the levels immediately above (where the Class 6 retail fire load sits below) and around openable balcony doors, keeping standard TMT for the upper, lower-risk levels — a graded response rather than one spec for the whole tower.
- **The connection is not new geometry.** This cavity-barrier detail and the balcony thermal break flagged in AT2.2 §4 (the balcony now needs ~2.25 m of cantilever, not 1.8 m, once the real 3.6 m bay is used) land at the same junction — the CLT wall edge, where the facade panel, the insulation, and the structural balcony connection all meet. Draw them together in AT2.4, not as unrelated details on separate sheets.

| Facade fire interface | Risk if undetailed | Response |
|---|---|---|
| Cavity behind TMT panel | Fire runs floor-to-floor inside the void | Intumescent cavity barrier at every floor line |
| TMT panel face | Combustible (Class B/C untreated) | Fire-treated (B-s1,d0) at podium + around openings |
| CLT wall edge / balcony junction | Char, thermal break, and cavity barrier all competing for the same 100–150 mm zone | Coordinate as one detail, not three (AT2.4) |
| Sprinkler coverage | — | Confirms E1D6 trigger already covers the facade cavity per AS 2118.1 |

---

*Sourced from: Week 6 Revit model sheet A400 (member sizes, "Fire protection: Char-design/encapsulation" note); AS 1720.4 char-rate convention (~0.7 mm/min softwood glulam); AT1.4 structural system report (B1P1, E1D6 sprinkler trigger); `AT2-facade-panel-strategy.md` (TMT fire classification, from the studio's facade-panel comparison).*
