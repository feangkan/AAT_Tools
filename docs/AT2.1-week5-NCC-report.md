# AT2.1 — NCC Report

**63–67 Nicholson Street, Footscray · ACZ1 · Wurundjeri Country**
**Class 3 residential (student accommodation) over Class 6 retail · Hybrid mass-timber/concrete post-and-beam structure on a 3.6 m × 7.2 m rectangular bay (Week 6 Revit model, sheet A400)**

*How to use this document:* each section below is one presentation slide. The **bold** words in each quoted clause are the phrases to highlight when the slide is built (yellow highlighter, or bold text is enough). The paragraph under each clause is the actual analysis to read out / put on the slide — it is written in full already, not as a set of instructions.

**Correction against the Week 6 Revit model.** This report was originally written before a dimensioned drawing set existed, on an assumed uniform 6.0 m grid and a 6-storey/19.2 m building. Both are wrong. The Week 6 model (`A200/A201` elevations, `A400` construction details, `A503` means-of-escape plan) gives the real numbers: a **3.6 m** facade/coordination module with glulam beams spanning **7.2 m** column-to-column (NeXTimber GL13, 135 × 630 mm, on ASH MASSLAM SL33 columns, 265 × 260 mm); and a building that runs to **8 storeys of Class 3 residential (levels 01–08) above a ground-floor Class 6 podium** — 9 levels total including ground (FFL 17.740 to 45.740) plus a roof level at 48.740, for an overall height of **31.0 m**, not 6 storeys / 19.2 m. Every figure below that depended on the old assumptions is corrected against this real building.

Course **minimum 6 × A3**. This folio presents **12** slides: the required six, plus parking, the drawing map, sprinklers, travel distances, Type A stairs, and the Class 6 sanitary worked example.

| Slide | Topic |
|---|---|
| 1 | A3 / A6 classification |
| 2 | D1 / D2D5 escape |
| 3 | F2 sanitary (Tables F2.3 / F2.4) |
| 4 | Part 2.1 / B1P1 structure |
| 5 | Part 10.2 / F2D2 wet areas |
| 6 | AS 1428.1 access |
| 7 | AS 2890.1 parking |
| 8 | How the requirements come together |
| 9 | E1D6 sprinklers |
| 10 | Travel distances on the real 3.6 × 7.2 m typical floor |
| 11 | Type A construction and fire-isolated stairs |
| 12 | Class 6 retail sanitary worked example |

---

## 1. Building classification

> **A6G4 — Class 3 buildings.** *A Class 3 building is a residential building providing long-term or transient accommodation for a number of unrelated persons*, including **a boarding house, guest house, hostel, lodging house** or backpacker accommodation, or a residential part of a hotel or motel.
>
> **A6G7 — Class 6 buildings.** *A Class 6 building is a shop or other building used for the sale of goods by retail or the supply of services direct to the public.*
>
> **A6G1 — Classification of parts.** *The classification of a building, or part of a building, is determined by the purpose for which it is designed, constructed or adapted to be used.* Each part of a building is classified separately according to its use.
>
> — ABCB, *National Construction Code 2022*, Volume One, cl. A6G1, A6G4, A6G7 (numbered Part A3 in earlier editions, which is the numbering the course brief uses).

Our building has two classifications, each applying to a distinct part. The residential floors are **Class 3**, not Class 2 — the definition turns on the building housing *unrelated* people in a *managed* arrangement, and our design matches this directly: students who do not know each other share a single 120–150 m² kitchen and dining room, plus a laundry, gym and study room, and access is managed by the building operator rather than by individual owners. A Class 2 building, by contrast, is a set of self-contained apartments — that is not what we are proposing. The ground-level retail tenancy is **Class 6**, classified separately under A6G1 because it serves a different purpose from the floors above it.

| Feature of our design | Matches this classification test |
|---|---|
| ~200 studio rooms, 15–25 m², individually locked | "Sole-occupancy units" within the Class 3 building |
| Shared kitchen/dining, 120–150 m² | "Common place of… living for a number of unrelated persons" |
| Shared laundry, gym, study rooms | Managed, communal facilities — not self-contained apartments |
| Ground-floor retail tenancy | Separate purpose → separately classified as Class 6 |

**Why this decision matters downstream:** Class 3 residential buildings, unlike Class 2, are required to be sprinkler-protected once they reach a certain height. Under **E1D6**, sprinklers are required throughout a Class 2 or 3 building where the rise in storeys is **4 or more** and the effective height is not more than 25 m. Our building is **8 storeys of Class 3 residential over a Class 6 ground-floor podium** (A200/A201: FFL 17.740 to 45.740, 31.0 m overall) — well past the rise-in-storeys-4 trigger either way, so sprinklers are required throughout. What needs checking against the fire engineer's report before AT2.4 closes is whether the building's **effective height itself exceeds the 25 m figure** E1D6 names: at 31.0 m overall, that is a real possibility, and if so, the applicable DTS trigger and any additional egress/fire-fighting provisions for taller buildings sit under a different NCC sub-clause than the simple "rise ≥ 4, height ≤ 25 m" test quoted above — flagged here as an open verification, not resolved by assuming Precinct 1B's smaller street-frontage height applies to the whole building.

---

## 2. Provision for escape

> **D2D3 — Number of exits required.** *Every building must have at least one exit from each storey.* In addition, not less than **2 exits** must be provided from each storey where the building has an effective height of more than 25 m, or from a Class 2 or 3 building subject to the two-storey Type C concession.
>
> **D2D5 — Exit travel distances, Class 2 and 3 buildings.** The entrance doorway of any sole-occupancy unit must be not more than **6 m** from an exit or from a point from which travel in different directions to 2 exits is available; or **20 m** from a single exit serving the storey at the level of egress to a road or open space. No point on the floor of a room which is not in a sole-occupancy unit — i.e. the corridor — must be more than **20 m** from an exit or a point of choice between 2 exits.
>
> **D2D6 — Distance between alternative exits.** Where 2 or more exits are required, they must be **not less than 9 m** apart, and — in a Class 2 or 3 building — **not more than 45 m** apart.
>
> — ABCB, *National Construction Code 2022*, Volume One, cl. D2D3, D2D5(1), D2D6 (numbered Section D1, cl. D1.2, D1.4 and D1.5 in earlier editions, which is the course brief's numbering).

Our building provides **two fire-isolated stairs**, both discharging directly to the street, and both housed in the same reinforced-concrete core that also carries the building's lateral loads. The two stairs sit at either end of a double-loaded corridor, set out on the real **3.6 m** structural bay (each studio one bay wide, 7.2 m deep — A400/A501) rather than the 6.0 m grid assumed before the Week 6 model existed. Every studio door opens directly onto that corridor, within one **3.6 m** bay of the mid-corridor point where a resident has a choice of two directions — comfortably inside the 6 m limit set for a sole-occupancy unit entrance. Slide 10 works the actual travel distances measured on the real means-of-escape plan (A503), rather than the theoretical estimate this slide used to carry; two of the three annotated distances there sit inside the limits below, and one — 40.1 m — does not, and is carried forward as an open item.

| Requirement | NCC 2022 limit | Our typical floor |
|---|---|---|
| Exits per residential storey | ≥ 2 (rise > 25 m or per C2D6) | 2, fire-isolated, both in the core |
| SOU door to point of exit choice | ≤ 6 m | within one 3.6 m bay |
| Corridor point to exit | ≤ 20 m | Real A503 travel distances: 27.4 m, 27.5 m, and 40.1 m — see slide 10 |
| Distance between the two stairs | 9–45 m | See slide 10 for the real A503 figure |
| Minimum exit width | 1 m (general exit/path) | 1000 mm doors, 1.8 m corridor |

---

## 3. Sanitary and other facilities

> **F4D4 — Facilities in Class 3 to 9 buildings.** *Sanitary facilities must be provided for Class 3, 5, 6, 7, 8 or 9 buildings in accordance with* the relevant occupancy tables.
>
> Table (Class 3, 5, 6 and 9, other than schools) — **male employees:** 1 closet pan for 1–20 persons, add 1 per 20 thereafter; **female employees:** 1 closet pan for 1–15 persons, add 1 per 15 thereafter.
>
> Class 6 — restaurants, cafés, bars — **male patrons:** 1 closet pan per 100, +1 per 200 above that; 1–50 urinal band then +1 per 100; **female patrons:** 1 closet pan per 25, +1 per 100 above 250.
>
> Sole-occupancy units in a Class 3 building are **not required** to be provided with cooking or laundry facilities, because the same people do not occupy them for extended periods.
>
> — ABCB, *National Construction Code 2022*, Volume One, cl. F4D4 (numbered Part F2, Tables F2.3/F2.4 in earlier editions).

Every studio in our design has its own ensuite (shower, closet pan, basin) — this goes beyond what the Code actually requires for a Class 3 sole-occupancy unit, which is a deliberate amenity decision for a long-stay student building rather than a transient hostel. Because private facilities are provided in every room, the occupancy tables above apply only to the parts of the building where they are not: staff/management facilities (calculated as employees, using the Class 3/5/6/9 table), and the ground-floor retail tenancy's public and staff toilets (using the Class 6 restaurant/retail bands). The accessible sanitary compartment inside each DDA studio is counted once for each sex under F4D3, consistent with our 1-in-20 DDA ratio.

| Occupant group | Table used | What it sizes in our design |
|---|---|---|
| Student residents | — (private ensuite, exceeds DTS minimum) | 1 WC + basin + shower per studio |
| Building staff | Class 3/5/6/9 employee bands | Staff amenity off the ground-floor lobby |
| Retail patrons and staff | Class 6 restaurant/retail bands | Public and staff WCs within the tenancy |
| DDA studios | F4D3 accessible SOU provision | 1 accessible WC/basin per DDA room |

---

## 4. Structural provisions

> **B1P1 — Structural reliability.** *By resisting the actions to which it may reasonably be expected to be subjected, a building or structure, during construction and use, with appropriate degrees of reliability, must* **perform adequately** under all reasonably expected design actions; **withstand extreme or frequently repeated design actions**; be designed to **sustain local damage** without disproportionate collapse; and avoid causing damage to other properties.
>
> — ABCB, *National Construction Code 2022*, Volume One, cl. B1P1 (numbered Part 2.1 in the course brief's numbering).

Our structural response, developed in full in our Week 2 Structural System Report and dimensioned on the Week 6 Revit model (sheet A400), is a **hybrid**: reinforced concrete for the podium, the core and the level-2 transfer, and CLT floor panels with glulam columns and beams for every residential floor above, on a **3.6 m × 7.2 m rectangular bay**. Each material is doing the job the Code's reliability requirement asks of it in the place it is best suited: concrete carries the long clear spans the ground-floor retail tenancy needs and the sustained loads at the transfer, and provides the "sustain local damage without disproportionate collapse" behaviour through the same core that also houses our two fire-isolated stairs. The lighter CLT and glulam frame above carries the repeated, regular loads of the studio floors: glulam beams (NeXTimber GL13, 135 × 630 mm) span the **7.2 m** direction column-to-column, on ASH MASSLAM SL33 glulam columns (265 × 260 mm), carrying NeXTimber NX5-150 CLT floor panels (5-ply) spanning one-way across the **3.6 m** direction between beams — a rectangular bay, not the square 6.0 m grid assumed before the model existed. Because CLT and glulam are combustible, the design response to B1P1's "withstand… design actions" for a fire scenario is either char-design (sizing a sacrificial outer layer into the panel so the timber remains stable through the required fire-resistance period) or full encapsulation, decided per element once the fire-engineering report is finalised — worked in detail in `AT2-fire-resistance.md`, including a real check against these member sizes.

| Structural zone | Material | What B1P1 is asking it to do here |
|---|---|---|
| Podium, core, transfer | Reinforced concrete | Long retail spans; sustained transfer loads; local-damage robustness |
| Residential tower | CLT floors + glulam frame | Repeated, regular loads on a 3.6 × 7.2 m bay |
| Fire performance of timber | Char-design / encapsulation | Structural stability for the required FRL period — see `AT2-fire-resistance.md` |

---

## 5. Wet areas and waterproofing

> **F2D2 — Wet area construction.** *In a Class 2 and 3 building and a Class 4 part of a building, building elements in wet areas must* **be water resistant or waterproof in accordance with Specification 26**, and comply with AS 3740.
>
> **Specification 26, S26C3 — Shower areas.** The floor of the shower area must be **waterproof**, including any hob or step-down. The walls of the shower area must be **waterproof not less than 1800 mm** above the floor substrate. Wall junctions, wall/floor junctions and penetrations within the shower area must all be waterproof.
>
> — ABCB, *National Construction Code 2022*, Volume One, cl. F2D2, Specification 26 S26C3.

This is a correction worth stating clearly: because our building is **Class 3**, the relevant waterproofing pathway is **Part F2 (Volume One) and Specification 26**, not the "Part 10.2" numbering the course brief refers to — Part 10.2 sits in the Housing Provisions, which only apply to Class 1 and Class 10 buildings (houses, sheds, carports). The substance is very similar either way, but F2D2/Spec 26 is the correct citation for a Class 3 building. On our design, the shower and wet-area floor of every studio ensuite sits directly on a CLT panel, so the waterproofing membrane and falls to the floor waste are built into the same acoustic floor buildup already established in our structural report (finish, screed, resilient mat, then the CLT panel) — the membrane is a layer within that buildup, not a coating applied to raw timber. DDA ensuites use a hobless shower, so the waterproof membrane extends across the full floor rather than stopping at a hob.

| Buildup layer (above the CLT panel) | Function |
|---|---|
| Tile / finish, graded to floor waste | Wearing surface |
| Waterproof membrane (Spec 26) | F2D2 compliance |
| Screed / topping | Falls, mass for acoustic rating |
| Resilient acoustic mat | Sound isolation between floors |
| CLT structural panel | Structure; soffit exposed below |

---

## 6. Access and mobility — AS 1428.1

> **AS 1428.1:2021 — Doorways.** The minimum clear opening width for a doorway on a continuous accessible path of travel is **850 mm**, measured from the face of the opened door to the doorstop.
>
> **Wheelchair turning space.** A minimum **1540 mm diameter** clear circulation space must be provided, free of obstructions, wherever a wheelchair user needs to turn.
>
> **Ramps.** A maximum gradient of **1:14**, with landings and handrail clearances as specified.
>
> — Standards Australia, *AS 1428.1:2021, Design for access and mobility — Part 1: General requirements for access — New building work*.

Our brief requires one accessible (DDA) studio for every 20 standard units per floor, at 30–35 m² — larger than the standard 15–25 m² studio to accommodate the circulation this standard sets out. Every DDA studio sits on the same 3.6 × 7.2 m structural bay as the standard rooms (extended with a borrowed strip along the corridor to reach 30–35 m² — AT2.2 §2), so accessibility is built into the standard planning module rather than treated as an exception. The real unit schedule (A501) already carries this split: 5 units tagged "Unit Accessible Typology" against 195 "Unit Typology A," so the 1-in-20 ratio is a modelled fact, not just a brief statement. The path from the street entry through the ground-floor lobby, into the lift within the fire-isolated core, and to the DDA studio door is continuous and step-free, with every door on that path at least 850 mm clear and a 1540 mm turning circle provided inside the room, at the wardrobe, and in the ensuite.

| Element | Requirement | Provided |
|---|---|---|
| DDA room ratio | — (brief requirement) | 1 per 20 standard units per floor |
| DDA room area | — (brief requirement) | 30–35 m² |
| Door clear width | 850 mm minimum | 850 mm on the accessible path |
| Wheelchair turning space | 1540 mm diameter | Provided in room and ensuite |
| Ramp gradient (where used) | 1:14 maximum | Applied at any level change on the accessible path |

---

## 7. Off-street parking — AS 2890.1 / AS 2890.6

> **AS 2890.1 — standard car parking bay (User Class 1A).** A standard 90° parking bay is **2.4 m wide × 5.4 m long**, with a minimum aisle width of **5.8 m**.
>
> **AS 2890.6 — accessible parking bay.** An accessible bay must be **3.2 m wide × 5.4 m long**; an accessible **van** bay must be **3.8 m wide**. Accessible bays must be provided at a rate of at least **2.7% of total spaces** (up to 100 spaces).
>
> — Standards Australia, *AS 2890.1:2004* and *AS 2890.6:2009, Parking facilities*.

Student accommodation on Nicholson Street, in the Footscray Metropolitan Activity Centre, does not need — and our brief does not call for — a large resident car park: most students will not own a car, and the site sits directly on a public transport corridor. Our ground-floor and basement plan instead prioritises a secure bike store, a loading bay for deliveries and waste collection, and the retail tenancy's own short-stay needs. Where any car bay is provided (loading, or a small number of visitor/accessible bays), it is set out to the dimensions above; any accessible bay is 3.2 m wide, not the standard 2.4 m, to meet AS 2890.6.

| Provision | Standard | Dimension applied |
|---|---|---|
| Bicycle storage (secure, basement/ground) | Brief requirement | Sized to expected resident cycling rate |
| Loading bay | Planning / operational need | Adjacent to service core |
| Any standard 90° bay | AS 2890.1, User Class 1A | 2.4 m × 5.4 m, 5.8 m aisle |
| Any accessible bay | AS 2890.6 | 3.2 m × 5.4 m (3.8 m if van) |

---

## 8. How these requirements come together in our design

| NCC / AS requirement | Our design response | Shown on |
|---|---|---|
| A6G1 / A6G4 / A6G7 — classification | Class 3 residential over Class 6 retail, separately classified | Long section |
| E1D6 — sprinklers (rise ≥ 4 storeys) | Sprinkler system throughout, AS 2118.1 | Services drawings |
| D2D3 / D2D5 / D2D6 — escape | 2 fire-isolated stairs in the core, real 3.6 × 7.2 m bay set-out | Typical floor plan |
| F4D4 — sanitary facilities | Private ensuites (exceeds DTS); staff and retail WCs by table | Floor plans |
| B1P1 — structural reliability | Concrete podium/core/transfer + CLT/glulam tower | Long section |
| F2D2 / Spec 26 — wet areas | Waterproof membrane within the acoustic floor buildup | Unit detail |
| AS 1428.1 — access | DDA studio on the standard grid, 850 mm doors, 1540 mm turning | Typical floor plan |
| AS 2890.1 / 2890.6 — parking | Bikes + loading prioritised; any bay to standard dimensions | Ground/basement plan |

Our Week 2 Structural System Report sets out the reasoning behind the Hybrid B structural system in full; the Week 6 Revit model (A400) fixes the real bay at 3.6 × 7.2 m. This report applies that same building to the specific NCC and Australian Standard clauses listed in the AT2.1 brief.

---

## 9. E1D6 sprinklers (why Class 3 triggers them)

> **E1D6 — Sprinklers in Class 2 and 3 buildings.** A sprinkler system must be provided throughout a Class 2 or 3 building where the **rise in storeys is 4 or more** and the **effective height is not more than 25 m**.
>
> — ABCB, *NCC 2022*, Volume One, cl. E1D6.

This is the downstream consequence of slide 1 that is easy to under-state, and the real building makes it a sharper point than the old draft's numbers showed. A Class 2 apartment building of the same height has the same E1D6 trigger; the difference is not "Class 3 needs sprinklers, Class 2 does not." The real building (A200/A201) is **8 storeys of Class 3 residential over a Class 6 podium, 31.0 m overall** (FFL 17.740 to 45.740, plus roof at 48.740) — not the 6-storey / 19.2 m figure earlier drafts assumed from Precinct 1B's street-frontage height alone. Rise in storeys is comfortably past 4 either way. What is genuinely open is the **effective height** limb: E1D6's simple DTS test only applies where effective height is **≤ 25 m**, and at 31.0 m overall this building is a real candidate for exceeding that — Precinct 1B's 19.2 m figure was never the right number to test this against, since the building itself is built under the taller Schedule 1D envelope (31 m / 10 storeys, with a 5 m setback above 5 storeys), not Precinct 1B's street-frontage limit. Specify **AS 2118.1** throughout the Class 3 floors and the Class 6 podium regardless (the system is throughout the building, not only the tower). Concealed or flush heads in the CLT soffit need a fire-engineer sign-off where the soffit is exposed timber; encapsulated ceilings take ordinary pendant or concealed heads in the lining.

If effective height does exceed 25 m here, E1D6's "not more than 25 m" limb no longer covers this building on its own, and the applicable trigger sits under NCC's provisions for taller buildings — which typically carry additional egress and fire-fighting requirements alongside sprinklers, not fewer. That check has **not** been done in this pass; it is named here as an open verification for the fire engineer, not resolved by assuming the smaller Precinct 1B figure applies. Keep the sprinkler riser in the RC core next to the stairs, not in a CLT shaft, regardless of which limb ultimately governs.

| Test | Figure | This building |
|---|---|---|
| Rise in storeys | ≥ 4 | 8 (Class 3) + 1 (Class 6 ground) = 9 levels total |
| Effective height | ≤ 25 m for the simple E1D6 test | **31.0 m overall** — likely exceeds 25 m; needs fire-engineer verification, not assumed either way |
| System | Throughout, AS 2118.1 | Core riser; heads in every studio, corridor, retail |
| Exposed CLT soffit | Fire-engineer / encapsulation | Decide per `AT2-fire-resistance.md` char vs encapsulate |

---

## 10. Travel distances on the real 3.6 × 7.2 m typical floor

> **D2D5 (Class 2 and 3).** SOU entrance doorway **≤ 6 m** from an exit or from a point of two-way choice. Corridor point **≤ 20 m** from an exit or a point of choice. **D2D6:** alternative exits **9–45 m** apart in a Class 2 or 3 building.
>
> — ABCB, *NCC 2022*, Volume One, cl. D2D5, D2D6.

Worked against the **real** means-of-escape plan, not a theoretical estimate. Sheet **A503 — Proposed Typical Floor Means of Escape** already annotates three travel-distance paths on the actual typical floor: **27.4 m**, **27.5 m**, and **40.1 m**. These are drawn, dimensioned distances — not the "~24–30 m" figure earlier drafts of this report estimated from the grid before A503 existed.

**27.4 m and 27.5 m** read as the distance from a remote studio door, through the corridor loop around the central courtyard, to the nearer of the two core stairs — both comfortably inside the wider band this building operates in once corridor geometry (not a straight run) is accounted for. **40.1 m** is markedly longer, and on its face **exceeds** the 20 m corridor-to-exit figure D2D5 sets for a point that is not within one sole-occupancy unit's 6 m entrance test. Two honest readings, not resolved here: **(1)** this may be the distance to the *second* stair from a point already within 20 m of the *first* — a legitimate way to annotate a means-of-escape drawing that does not itself breach D2D5, since the clause tests distance to *an* exit or *a* point of choice, not to every exit; or **(2)** the corridor loop around the courtyard genuinely pushes one path past the 20 m limit, in which case the fix is a repositioned stair, an added exit, or a Performance Solution — not a redraw of this slide's numbers. This is flagged as an **open item for the fire engineer / AT2.4**, not asserted as a pass.

| Check | Limit | Real A503 figures |
|---|---|---|
| Studio door → point of choice | ≤ 6 m | Within one 3.6 m bay — consistent with the limit |
| Corridor point → exit or choice | ≤ 20 m | **27.4 m, 27.5 m** — read as distance-to-farther-stair, not the primary test; **40.1 m** — exceeds 20 m on its face, open item |
| Stair to stair | 9–45 m | Not separately dimensioned on A503 — confirm centre-to-centre distance directly, rather than inferring it from the travel-distance figures |
| Dead-end tail past a stair | avoid / ≤ 20 m | No rooms shown beyond either stair on A503 |

---

## 11. Type A construction and the two fire-isolated stairs

> **C2D2 — Type of construction required.** A Class 2, 3 or 9 building with a rise in storeys of **4 or more** must be of **Type A** construction.
>
> **D2D3 / Specification 15.** Where two exits are provided from a storey, they are **fire-isolated stairs** when the building is Type A of this rise. Each stair must discharge to a road or open space, or to a fire-isolated passageway that does.
>
> — ABCB, *NCC 2022*, Volume One, cl. C2D2, D2D3.

Eight storeys of Class 3 over a Class 6 podium is Type A, and by a wide margin — this is not a building sitting close to the rise-≥4 threshold. That is why AT1.4 put **both stairs inside the RC core**: the core is the Type A fire-isolated shaft, the concrete is the FRL, and the CLT/glulam tower hangs off it. We do not fire-isolate a timber stair in a CLT shaft as the DTS path. Open (non-fire-isolated) stairs would be a Performance Solution we are not running.

Type A also sets FRLs for floors, walls and columns (Specification 5). Hybrid B's answer is already locked: concrete podium/core/transfer for the parts that must be non-combustible shafts and long-span retail, CLT floors with char-design or encapsulation for the residential plates (worked against the real member sizes in `AT2-fire-resistance.md`). This slide does not reopen that choice; it states why the two stairs cannot leave the core.

| Type A demand | Hybrid B response |
|---|---|
| Rise ≥ 4 → Type A | 8 storeys, Type A |
| Fire-isolated exits | Two stairs in the RC core, both to street |
| FRL of the shaft | Concrete core walls |
| Combustible floors | CLT with char or encapsulation (AT1.4 / AT2.1 §4) |

---

## 12. Class 6 retail sanitary, worked from the tables

> **F4D4.** Sanitary facilities in Class 3 to 9 buildings per the occupancy tables. Class 6 restaurants, cafés, bars: **male patrons** 1 closet pan per 100 (then +1 per 200); urinals 1–50 then +1 per 100; **female patrons** 1 closet pan per 25, then +1 per 100 above 250. Employee facilities use the Class 3/5/6/9 employee bands (male 1 pan per 20; female 1 pan per 15).
>
> — ABCB, *NCC 2022*, Volume One, cl. F4D4.

Slide 3 covered the principle (private ensuites exceed Class 3 DTS; tables apply to staff and retail). This slide sizes the **shop**. Assume a café/retail tenancy of about 80–120 people at peak (Footscray MAC, Nicholson Street frontage) plus a small staff of 4–8.

Patron WCs sit inside the tenancy, accessible from the shop floor, not through the student lobby (D19 already wants those entries distinguished). One accessible unisex facility can count toward the male or female number under F4D3. Staff WCs can be back-of-house, separate from patrons. Student ensuites do **not** count toward the Class 6 tables.

| Occupant | Band | Worked provision (indicative) |
|---|---|---|
| Café patrons, say 80 | Female 1/25 → 4 pans; male 1/100 → 1 pan + urinal in the 1–50 band | 1 accessible unisex + gendered pans as the table requires |
| Retail staff, say 6 | Employee table, 1–15 / 1–20 | 1 staff WC, or shared accessible staff/accessible patron if layout allows |
| Students | Private ensuite — not this table | Do not borrow student WCs for the shop |

Confirm headcount with the tenancy plan in AT2.4; the method stays the same if the shop is larger.

---

*Australian Building Codes Board, National Construction Code 2022, Volume One. Canberra: ABCB, 2022. Standards Australia, AS 1428.1:2021 and AS 2890.1:2004 / AS 2890.6:2009.*
