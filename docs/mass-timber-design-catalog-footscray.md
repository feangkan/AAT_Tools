# Mass Timber Design Catalog — Footscray Student Accommodation

**Project:** 63–67 Nicholson St, Footscray · ARCH3372 · Class **3** residential + Class **6** retail  
**System:** Hybrid — **RC (or steel) podium** + **CLT floors + glulam frame** residential tower  
**Use:** Start-to-finish design catalog · A3 landscape · each topic = **TEXT zone + PICTURE zone**  
**Companion:** NCC fire/egress → [`NCC-design-catalog-footscray.md`](./NCC-design-catalog-footscray.md) · FAR/height → [`AT1.2-density-FAR-footscray.md`](./AT1.2-density-FAR-footscray.md)

> **Layout rule (every content block):** Left/top = **TEXT** (narrative + table + actions). Right/bottom = **PICTURE** (screenshot / drawn diagram). Caption image with source (Chicago short). Manual paste — Claude cannot extract PDF images.

---

## Catalog map

| Phase | Sheets | Focus |
|-------|--------|-------|
| **A · Why timber** | 01–03 | Brief fit, carbon, comparison |
| **B · Products** | 04–07 | CLT, glulam, other MT, grades |
| **C · Systems** | 08–11 | Bearing wall, post-beam, plate, **hybrid** |
| **D · Project application** | 12–16 | Grid, floor, section, core, load path |
| **E · Performance** | 17–21 | Fire, acoustic, moisture, thermal, services |
| **F · Detail & build** | 22–26 | Connections, junctions, prefab, sequence |
| **G · Country & close-out** | 27–29 | Supply/Country, checklist, refs + FIND IT |

---

# MASTER IMAGE INDEX (screenshot these)

| Local PDF | GitHub | Best pages for pictures |
|-----------|--------|-------------------------|
| `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf` | [link](https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/5-MassTimberPedagogy-101-StructuralBasics.pdf) | p.13 family; **p.14 CLT**; p.18 glulam; **p.26** bearing wall; **p.27** post-plate; **p.28** post-beam; **p.29–30** hybrid |
| `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` | [link](https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/6-MassTimberPedagogy-101-StructuralDesign.pdf) | Design module diagrams throughout |
| `resources/klh-building-system-multi-story-residential-buildings.pdf` | [link](https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/klh-building-system-multi-story-residential-buildings.pdf) | System axon, floor build-ups, connections |
| `resources/klh-residential-en.pdf` | [link](https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/klh-residential-en.pdf) | Residential interiors / elevations |
| Brief | `project-information/AAT_project_brief.pdf` | Program numbers for text |
| Web | Brock Commons Tallwood House (Acton Ostry / UBC) | Hybrid tall timber student housing precedent — credit architect |
| Web | WoodSolutions / FWPA Australia | AU industry guidance (secondary) |

**Repo root:** https://github.com/feangkan/AAT_Tools/tree/cursor/aat-tools-resources-3c74

---

# PHASE A — WHY MASS TIMBER

## SHEET 01 — Project brief → structural problem

### TEXT
**Narrative**  
200+ student studios + communal kitchen/laundry/gym + Class 6 retail + ≥50% ground open space. Need a repetitive residential plate, fast construction, lower embodied carbon, and fire-safe mixed-use separation.

**Design drivers**

| Driver | Implication for structure |
|--------|---------------------------|
| Class 3 lodging | Sprinklers, dual stairs, FRL — see NCC catalog |
| Class 6 podium | Longer spans, higher fire load → concrete/steel |
| Studios 15–25 m² | Module ~3.0–3.6 m → grid 6.0 / 7.2 m |
| FTC ≥ 2.7 m | Limit structure + acoustic + sprinkler depth |
| 5% + 10% allowances | Core / risers sized early |
| Prefab | CLT panels + glulam suit student-housing repetition |

**Selected system:** Hybrid RC podium + CLT/glulam tower.

### PICTURE
- Site / brief diagram (brief PDF p.1–2) **or** simple massing: podium + tower  
- **FIND IT:** `AAT_project_brief.pdf`; draw section if no photo

**Footer:** RMIT, *AAT Project Brief*. ARCH3372.

---

## SHEET 02 — Why mass timber for student housing

### TEXT
**Benefits for this typology**  
- Lower embodied carbon vs full RC  
- Prefabricated panels → speed, quality, less site noise in Footscray MAC  
- Warm exposed or semi-exposed interiors for long-stay rooms  
- Panelised floors align with double-loaded corridor plans  

**Challenges (design early)**  
Acoustic separation · fire encapsulation / Performance Solution · moisture during build · ceiling void for sprinklers · Australian supply lead times  

**One-line thesis**  
*Timber carries the Class 3 residential floors; concrete carries Class 6 retail, transfer, and fire separation.*

### PICTURE
- Side-by-side: timber interior student room vs concrete frame (from KLH residential PDF or web)  
- **FIND IT:** `klh-residential-en.pdf` early pages; Mass Timber PDF p.14 Brock Commons photo caption

**Footer:** KLH; Mass Timber Pedagogy Module 1.

---

## SHEET 03 — Options comparison (select hybrid)

### TEXT

| | Mass timber hybrid ✓ | Full RC | Steel + slab |
|--|----------------------|---------|--------------|
| Embodied carbon | Low–med | High | Med |
| Prefab / speed | High | Low | Med–high |
| Class 6 retail spans | Podium RC/steel | Easy | Easy |
| Class 3 character | Strong | Neutral | Industrial |
| Fire path | Encapsulation + sprinklers | Familiar | Encasement |
| Grid (working) | **6.0–7.2 m** | 8.0–8.4 m | 7.5–9.0 m |
| Acoustic | Needs build-up | Good mass | Needs build-up |

**Recommendation (repo):** Hybrid concrete/steel podium + mass-timber residential tower (KLH precedents).

### PICTURE
- Comparison icons or hybrid cutaway  
- **FIND IT:** Mass Timber PDF **p.29–30** hybrid systems; or draw 3 columns

**Footer:** AAT Studio `details.py` structural_options. Mass Timber Pedagogy p.29–30.

---

# PHASE B — PRODUCTS

## SHEET 04 — Cross-laminated timber (CLT)

### TEXT
**What it is**  
Dimensional lumber laminated in alternating (perpendicular) layers → panel for floors, walls, roofs. Some two-way spanning. Dimensionally stable in plane; moisture movement mainly in thickness.

**Use on Nicholson St**  
- Primary **floor plates** above podium  
- Optional party walls / corridor walls (if bearing-wall scheme)  
- Roof panels where lightweight roof preferred  

**Working sizes (confirm manufacturer)**  
Thickness ~**160–200 mm** for residential spans on 6 m grid (span-dependent). Studio module width often half-grid (3.0–3.6 m).

### PICTURE
- CLT layup diagram + building photo  
- **FIND IT:** Mass Timber Basics **p.14** (CLT layup + Brock Commons note)

**Footer:** Kingsley, *Structural Basics of Mass Timber*, p.14.

---

## SHEET 05 — Glulam beams & columns

### TEXT
**What it is**  
Laminated timber lineal members; higher grades placed in high-stress zones. Beams and columns for post-and-beam frames.

**Use on Nicholson St**  
- Columns on **6.0 m grid**  
- Edge / corridor beams under one-way CLT  
- Transfer to steel base plates at podium  

**Working sizes (illustrative)**  
Columns ~280×280 mm or Ø300 mm; beams depth by span/load — engineer to **AS 1720**.

### PICTURE
- Glulam layup + beam/column photo  
- **FIND IT:** Mass Timber Basics **p.18**

**Footer:** Mass Timber Pedagogy Module 1, p.18. AS 1720.1.

---

## SHEET 06 — Other mass timber (know, then set aside)

### TEXT
Brief awareness for AT1.3/AT1.4:

| Product | Span | Note for this project |
|---------|------|----------------------|
| NLT / DLT | One-way | More moisture movement; less preferred for multi-storey PBSA |
| GLT panel | One-way | Similar issues; movement joints |
| LVL / LSL | One-way | Possible beams/rim boards |

**Decision:** Lead with **CLT + glulam** (KLH-type residential system). Mention others only as discarded options.

### PICTURE
- Product family overview  
- **FIND IT:** Mass Timber Basics **p.13**

**Footer:** Mass Timber Pedagogy Module 1, p.13.

---

## SHEET 07 — Species, grade, appearance

### TEXT
Species groups (e.g. SPF, DFL) affect strength **and** visual grade. Exposed timber = finish surface → specify visual grade early. Encapsulated timber = structural grade priority.

**AU note**  
Specify durability for weather-exposed elements (**AS 5604**). Course AT3.2 mentions Spotted Gum Class 1 / Group 1 fire-rated products for finishes — separate from primary CLT structure.

**Australia supply**  
Confirm local CLT/glulam producers and lead times in AT1.4 / Country note (PC36).

### PICTURE
- Species/grade table screenshot or timber sample board photo  
- **FIND IT:** Mass Timber Basics **p.5–8** (species / solid vs engineered); AS 5604 via Standards library

**Footer:** Mass Timber Pedagogy p.5–8. AS 5604.

---

# PHASE C — STRUCTURAL SYSTEMS

## SHEET 08 — Bearing wall systems

### TEXT
Vertical loads via walls (CLT or light frame). Efficient for stacked residential cells; party walls = structure + acoustic mass opportunity.

**Fit to studios**  
Good if party walls align floor-to-floor. Less flexible for future layout change and large communal openings.

**Project stance**  
Optional for tower wings; not exclusive — combine with frame at corridors.

### PICTURE
- Bearing wall diagram + residential example  
- **FIND IT:** Mass Timber Basics **p.26**

**Footer:** Mass Timber Pedagogy Module 1, p.26.

---

## SHEET 09 — Post-and-plate (point-supported)

### TEXT
Columns support flat CLT panels; no beams; shallow ceiling; large windows possible. Needs panel thickness for two-way span; column grid must match panel layout.

**Fit**  
Attractive for open communal floors; for dense studios, beams may still help services routing.

### PICTURE
- Post-and-plate diagram (Brock Commons type)  
- **FIND IT:** Mass Timber Basics **p.27**

**Footer:** Mass Timber Pedagogy Module 1, p.27. Brock Commons / Fast + Epp (credit).

---

## SHEET 10 — Post-and-beam (frame)

### TEXT
Beams span between columns; CLT (or other) as one-way deck. Flexible, open plans, good for corridor + room layout and MEP between beams.

**Project preference**  
**Primary recommendation** for Class 3 floors: glulam frame + CLT deck on **6.0 m** grid; double-loaded corridor.

### PICTURE
- Post-and-beam diagram  
- **FIND IT:** Mass Timber Basics **p.28**

**Footer:** Mass Timber Pedagogy Module 1, p.28.

---

## SHEET 11 — Hybrid systems (project default)

### TEXT
Hybrid = mass timber + concrete and/or steel to solve fire, lateral, long span, acoustics, or code.

**Nicholson St hybrid package**

| Level | Material | Role |
|-------|----------|------|
| Ground / L1 | RC frame + slab | Class 6 retail, loading, 50% open space structure |
| Transfer | RC beams/slab | Grid change; fire separation Class 6↔3 |
| Tower floors | CLT + glulam | Class 3 studios + communal |
| Core | RC (preferred) or encapsulated CLT | Stairs, lifts, lateral, FRL |
| Roof | CLT or light steel | Plant screen, PV optional |

### PICTURE
- Hybrid cutaway (timber + concrete/steel)  
- **FIND IT:** Mass Timber Basics **p.29–30**; KLH multi-storey PDF system axon

**Footer:** Mass Timber Pedagogy p.29–30. KLH *Multi-Story Residential*.

---

# PHASE D — APPLY TO THIS BUILDING

## SHEET 12 — Structural grid & studio module

### TEXT
**Primary grid:** **6.0 × 6.0 m** (alt. 7.2 m at lounges/study).  
**Studio bay:** 3.0–3.6 m wide × ~5.5 m deep ≈ 15–25 m².  
**DDA bay:** ~4.2 × 7.6 m ≈ 32 m² (1 per 20 units/floor).

Grid must align CLT panel joints, column centres, and facade modules (≥10% WFR daylight).

### PICTURE
- Typical floor grid overlay on unit plan  
- **FIND IT:** Draw in Revit/Canva; optional plan from AAT Generators SVG

**Footer:** RMIT Brief. AAT `details.py` grid_m [6.0, 7.2].

---

## SHEET 13 — Typical residential floor (timber)

### TEXT
Double-loaded corridor · central core · ~20 studios · dual fire stairs · lifts · level lounge 20 m².  
Timber zone = everything outside RC core/podium. Travel paths ≤ ~40 m (NCC D2 — see NCC catalog Sheet 03).

### PICTURE
- Annotated typical floor: timber hatch vs core hatch + travel dashes  
- **FIND IT:** Draw; D1 PDF only for egress diagram inset if needed

**Footer:** RMIT Brief. NCC Part D2 (companion catalog).

---

## SHEET 14 — Building section (hybrid)

### TEXT
Show: foundations → RC podium → transfer → timber storeys → roof plant.  
Label FTC 2.7 m, floor-to-floor ~3.2–3.4 m, sprinkler void, acoustic screed on CLT.

### PICTURE
- Full height section 1:200  
- **FIND IT:** Author drawing; reference KLH section if available in KLH PDF

**Footer:** Project section. KLH system (reference).

---

## SHEET 15 — Core & lateral system

### TEXT
RC core preferred for fire-isolated stairs, lift shafts, and wind/EQ lateral. Timber diaphragms (CLT floors) deliver lateral loads to core. Hold-downs / collectors at timber–concrete interface.

Allow **10%** fire/duct + **5%** services in plate/core planning.

### PICTURE
- Core plan + lateral load arrows  
- **FIND IT:** Draw; Mass Timber Module 2 PDF for diaphragm concepts if present

**Footer:** NCC D2 / Section C (companion). Brief 5%/10%.

---

## SHEET 16 — Gravity load path

### TEXT
Studio live/dead → finish/acoustic → **CLT** → **glulam beam** → **glulam column** → steel base / **RC transfer** → podium columns → foundations.

Annotate critical joints: CLT-to-beam, column-to-podium, beam-to-core.

### PICTURE
- Exploded axon or coloured load-path section  
- **FIND IT:** Draw; KLH connection photos for joint callouts

**Footer:** AS 1720.1. KLH connection details.

---

# PHASE E — PERFORMANCE

## SHEET 17 — Fire strategy for timber (Class 3)

### TEXT
Class 3 + multi-storey → sprinklers typical; encapsulate CLT/glulam **or** char Performance Solution; RC podium separates Class 6.  
Full clause FIND IT → NCC catalog Sheets 06–08.

**Timber-specific actions**  
Corridor faces encapsulated · shafts non-combustible/RC · document any exposed timber with fire engineer · cavity barriers at junctions.

### PICTURE
- Encapsulation wall/floor detail 1:5 + sprinkler in void  
- **FIND IT:** Draw detail; NCC online Sec. C screenshot optional inset

**Footer:** ABCB *NCC 2022* Sec. C & E. NCC Design Catalog Sheets 06–08.

---

## SHEET 18 — Acoustics on CLT

### TEXT
CLT alone is not enough for student rooms. Add resilient layer + floating finish; double linings to corridor; isolate gym/laundry.

| Junction | Build-up idea |
|----------|----------------|
| Studio–studio | CLT + resilient mat + screed/finish |
| Studio–corridor | Extra linings + acoustic door seals |
| Wet areas | Decouple services; avoid rigid pipe contact |

Targets: NCC Part F7 / Spec 28 (verify tables). Course AT3.2 expands products.

### PICTURE
- Layered floor/wall section  
- **FIND IT:** Draw; KLH acoustic build-up pages if in KLH PDFs

**Footer:** ABCB *NCC 2022* F7. AT3.2 brief.

---

## SHEET 19 — Moisture & durability

### TEXT
Wood moves with moisture (especially solid-sawn / NLT). CLT is more stable in plane but still needs dry storage, weather protection during erection, and vapour-smart walls.

**Design rules**  
Keep timber dry in transit/site · temporary roofs · detail balconies/drain so water cannot pond on CLT · DPCs at concrete interface · specify treatment/durability for any exterior timber (**AS 5604**).

### PICTURE
- Moisture movement diagram + fastener protrusion warning  
- **FIND IT:** Mass Timber Basics **p.11–12**, and CLT note on **p.14**

**Footer:** Mass Timber Pedagogy p.11–12, p.14. AS 5604.

---

## SHEET 20 — Thermal / facade interface

### TEXT
Timber reduces thermal bridging vs concrete balconies if detailed. Continuous insulation outboard of CLT/stud; window WWR for daylight (≥~10%) without overheating (Section J — NCC catalog Sheet 15).

Spotted Gum / timber batten rainscreen (course AT3.2) as cladding option over acoustic/fire build-up — not a substitute for structure.

### PICTURE
- Facade bay section: CLT / insulation / battens / window  
- **FIND IT:** Draw; `details.py` facade_templates wall_buildups

**Footer:** NCC Section J. AS 5604. AAT facade templates.

---

## SHEET 21 — Services coordination in timber

### TEXT
Prefer services in corridor ceiling void and vertical RC risers — minimise chasing CLT. Penetrations need fire-stop + acoustic seal. Sprinklers, ducts, lighting share **300–450 mm** void — protect 2.7 m FTC.

Hot water / HVAC: central plant on roof or basement; FCUs/VRF — see NCC catalog Sheets 16–17.

### PICTURE
- Corridor ceiling sandwich diagram  
- **FIND IT:** Draw (CLT / acoustic / void / sprinkler / ceiling)

**Footer:** Brief FTC 2.7 m. NCC E / J companion sheets.

---

# PHASE F — DETAIL & CONSTRUCTION

## SHEET 22 — Connections (typical)

### TEXT
Prefer **concealed plate / screw** connections (KLH-type) for fire and aesthetics. Design for installation tolerance and moisture shrinkage at fasteners.

**Three must-draw details**  
A Column base on RC pedestal  
B CLT floor to glulam beam  
C CLT to RC core (ledger / knife plate / angle)

### PICTURE
- Three 1:5 details  
- **FIND IT:** KLH multi-storey PDF connection pages; Mass Timber Module 2 if connection diagrams exist

**Footer:** KLH building system. AS 1720.1.

---

## SHEET 23 — Critical junctions

### TEXT
1. **Podium transfer** — timber column to RC beam (fire-stop, moisture break)  
2. **Balcony / edge** — thermal break, membrane, no water into CLT  
3. **Wet area** — ensuite membrane on topping above CLT (NCC F2 / Spec 26)  
4. **Roof edge** — parapet, overflow, plant isolation

### PICTURE
- Junction matrix photos/diagrams  
- **FIND IT:** Draw four callouts on section; wet area from NCC catalog Sheet 14

**Footer:** NCC Part F2 wet areas. Project details.

---

## SHEET 24 — Prefabrication & tolerance

### TEXT
CLT panels CNC-cut offsite; glulam cut to length; site = assemble + protect. Design for crane reach on Nicholson St (MAC constraints, HO overlays nearby). Panel max sizes from manufacturer — align with grid to reduce waste.

**Documentation**  
Panel plans, erection sequence, temporary bracing, moisture protection method statement (for AT1.4 / DD).

### PICTURE
- Prefab panel diagram or site photo (web / KLH)  
- **FIND IT:** KLH PDF; Mass Timber construction photos (credited)

**Footer:** KLH. Manufacturer panel limits (confirm).

---

## SHEET 25 — Construction sequence

### TEXT
1. Foundations + basement (if any)  
2. RC podium + core up  
3. Weather protect / transfer complete  
4. Erect timber floor-by-floor with temporary works  
5. Encapsulation / linings / services  
6. Facade + roof plant  

Coordinate fire stopping at each level before ascending.

### PICTURE
- Numbered sequence axon  
- **FIND IT:** Draw 6-step axon

**Footer:** Project construction narrative.

---

## SHEET 26 — Cost / carbon narrative (studio level)

### TEXT
Argument for folio (not a QS report): hybrid timber reduces structural carbon vs all-RC tower while podium handles retail/fire. Prefab may reduce programme risk. Trade-offs: acoustic toppings, fire linings, engineer fees for Performance Solutions.

Keep numbers qualitative unless you have LCA tools — cite WoodSolutions / EPDs if used.

### PICTURE
- Simple bar: embodied carbon comparison (schematic)  
- **FIND IT:** Draw bars; optional WoodSolutions diagram (attribute)

**Footer:** Qualitative carbon argument. WoodSolutions (if used).

---

# PHASE G — COUNTRY & CLOSE-OUT

## SHEET 27 — Designing with Country / supply (PC36)

### TEXT
Brief sits on **Wurundjeri Country**. For AT1.4: acknowledge Country; explore First Nations knowledge and **local/regional timber supply** — not token cladding only. Ask: who grew/harvested/milled; can structure or fitout use AU species responsibly; avoid greenwash.

Link open space (≥50% ground) planting to indigenous species (AAT Country module) — separate from structure but same folio story.

### PICTURE
- Country acknowledgment + timber supply map (AU) schematic  
- **FIND IT:** Brief Country text; AAT Country page concepts; supplier map drawn

**Footer:** RMIT Brief (Wurundjeri Country). PC36 / AT1.4 note in `details.py`.

---

## SHEET 28 — Start-to-finish checklist

### TEXT
**Schematic (AT1.4)**  
- [ ] Hybrid thesis written  
- [ ] Grid + typical floor  
- [ ] Section with load path  
- [ ] Fire encapsulation strategy stated  
- [ ] 3 connection details sketched  
- [ ] Precedent (KLH / Brock Commons) credited  

**DD (AT2)**  
- [ ] FRL / acoustic schedules  
- [ ] Manufacturer sizes locked  
- [ ] Wet area on CLT detailed  
- [ ] Erection sequence  

**Systems (AT3)**  
- [ ] Facade build-up on timber  
- [ ] Services void coordinated  
- [ ] Lighting/acoustic products  

### PICTURE
- Checklist graphic / stamp sheet  
- **FIND IT:** This list as large text on page

**Footer:** ARCH3372 deliverables map.

---

## SHEET 29 — Master FIND IT + bibliography

### TEXT — Where every picture lives

| Need | Open this | Pages / tip |
|------|-----------|-------------|
| CLT layup | `5-MassTimberPedagogy-101-StructuralBasics.pdf` | **p.14** |
| Glulam | same | **p.18** |
| Product family | same | **p.13** |
| Moisture | same | **p.11–12** |
| Bearing wall | same | **p.26** |
| Post-and-plate | same | **p.27** |
| Post-and-beam | same | **p.28** |
| Hybrid | same | **p.29–30** |
| Design depth | `6-MassTimberPedagogy-101-StructuralDesign.pdf` | skim for spans/connections |
| Residential system | `klh-building-system-multi-story-residential-buildings.pdf` | system + details |
| Residential photos | `klh-residential-en.pdf` | interiors/elevations |
| Program numbers | `AAT_project_brief.pdf` | p.1–3 |
| Fire clauses | NCC catalog + ncc.abcb.gov.au | Sec. C, E |
| Structure Code | NCC Part B1; **AS 1720.1** | library |
| Repo machine text | `backend/app/services/details.py` | structural_options |

**GitHub folder:**  
https://github.com/feangkan/AAT_Tools/tree/cursor/aat-tools-resources-3c74/resources

### PICTURE
- Collage of 4 key screenshots (CLT, hybrid, KLH axon, your section)  
- **FIND IT:** User-assembled from table above

### Bibliography (Chicago)

Kingsley, Gregory R. *Structural Basics of Mass Timber* (Structural Module 1). Mass Timber Pedagogy 101. File: `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf`.

*Structural Design with Mass Timber* (Structural Module 2). Mass Timber Pedagogy 101. File: `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf`.

KLH Massivholz GmbH. *Building System: Multi-Story Residential Buildings*. File: `resources/klh-building-system-multi-story-residential-buildings.pdf`.

KLH Massivholz GmbH. *Residential* (EN). File: `resources/klh-residential-en.pdf`.

Australian Building Codes Board. *National Construction Code 2022*. Volume One. https://ncc.abcb.gov.au/.

Standards Australia. *AS 1720.1 — Timber structures*.  
Standards Australia. *AS 5604 — Timber — natural durability ratings*.

RMIT University. *AAT Project Brief*. ARCH3372/2650.

Acton Ostry Architects / Fast + Epp. Brock Commons Tallwood House, Vancouver (precedent — credit on image).

**Footer:** Mass Timber Design Catalog · Footscray Class 3 + Class 6 · hybrid CLT/glulam.

---

## Squeeze / layout rules

- **A3 landscape**; each sheet = one topic.  
- **50/50 or 55/45** TEXT | PICTURE — never bury images under paragraphs.  
- Body ≤ ~120 words + one table.  
- Caption every image: *Source: Mass Timber Pedagogy Module 1, p.14.*  
- For AT1.4 six-pager, pack Sheets **01, 03, 11, 13–14, 17, 22** (or 11+12+14+17+22+28).

## Claude / Canva prompt

```
Build A3 landscape sheets from docs/mass-timber-design-catalog-footscray.md
for RMIT ARCH3372 Footscray hybrid mass timber Class 3 + Class 6 student housing.
Each sheet: separate TEXT area and PICTURE area.
User will paste images manually from resources/ PDFs using each sheet's FIND IT.
No page limit; follow sheet order 01–29; dense functional narrative.
```

---

*Mass Timber Design Catalog · ARCH3372 · start-to-finish · TEXT + PICTURE*
