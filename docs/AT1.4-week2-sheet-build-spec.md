# AT1.4 (Week 2) — Structural System Report: Sheet Build Spec

**Status:** Hybrid B (Mass Timber + Concrete) locked. This is the sheet-by-sheet content, in the repo's TEXT/PICTURE/footer format, ready to paste into Claude Design.
**Format:** A3 landscape, 420 × 297 mm · left = one diagram, right = ~80–120 word narrative · yellow-highlight 1–2 key phrases per sheet · Chicago footer refs on every sheet (no separate references page) · title block bottom-right: "63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/16"
**Minimum 6 sheets per the brief — this set runs to 16 because the brief's own requirement list (production, forms, connections, embodied energy, application, First Nations, plus acoustics and span justification you asked to add) doesn't compress into 6 without cutting content. See my questions at the end if you want it trimmed.**

Sources for each sheet are drawn from `docs/AT1.4-structural-system-report-final.md` (the full research) — this spec is the compressed, slide-ready version of that report.

---

### Sheet 01 — What is this building under the NCC?

**Narrative:** Classification follows **use**. Mixed building: **Class 3** student lodging above **Class 6** retail.
- **Class 3 (A6G4):** Long-term or transient accommodation for unrelated persons; hostel/lodging house.
- **Evidence:** communal kitchen 120–150 m²; studios 15–25 m² ensuite; shared laundry, gym, study.
- **A6G1:** each part classified separately; Class 3 + Class 6 permitted in one building.

**Diagram:** Section — Class 6 podium | Class 3 tower | fire separation line.
**Footer refs:** ABCB, *NCC 2022*, Vol. 1, A6G1, A6G4. RMIT, *AAT Project Brief*.
**Pull from:** `resources/NCC 2015 PART-A3 CLASSIFICATION OF BUILDINGS AND STRUCTURES.pdf`

---

### Sheet 02 — Chosen structural system: Hybrid B overview

**Narrative:** **Reinforced concrete carries the podium, core, and transfer level. CLT + glulam carry every residential floor above.** Not two systems bolted together — each material does the job it's best at: RC gives the fire-isolated core and long retail spans the podium needs; timber gives fast, light, repetitive residential floors.

| Element | Podium/core | Tower |
|---|---|---|
| Walls | RC perimeter + core | CLT party walls (optional) |
| Floors | RC transfer slab | CLT panels |
| Columns | RC, wide grid | Glulam |
| Beams | RC transfer beams | Glulam, 6.0 m grid |
| Roof | RC over core | CLT + glulam |

**Diagram:** Full-height section — RC podium/core, transfer slab, timber tower, labelled by element.
**Footer refs:** AT1.4 Structural System Report §1. KLH *Multi-Story Residential*.

---

### Sheet 03 — Classification consequences

**Narrative:** Class 3 accommodation serves unrelated occupants in a managed building — fire and egress requirements reflect that use.

| NCC issue | Consequence |
|---|---|
| Fire separation | Rated separation Class 6 ↔ Class 3 |
| Sprinklers | Class 3, 2+ storeys → sprinklers throughout |
| D1 | Min. 2 fire-isolated exits |
| B1/2.1 | Structure + FRL support fire strategy |
| AS 1428.1 | DDA 1:20 on Class 3 floors |

**Outcome:** RC podium + timber tower only works if the fire strategy is shown, not assumed.

**Diagram:** Class 3 → sprinklers + dual stairs + podium fire wall → hybrid structure.
**Footer refs:** ABCB, *NCC 2022*, A6G4; Sec. C; D1.

---

### Sheet 04 — Escape (D1) with typical floor plan

**Narrative:** Plan organised for escape before fire spread. ~20 rooms/floor → **two fire-isolated stairs**.
- ≥2 exits · travel ≤~40 m · dead-end ≤~20 m · exit width ≥1000 mm · corridor 1.8–2.0 m
- Brief 10% fire/duct allowance in cores/shafts

**Diagram:** Typical floor — core, 2 stairs, dashed travel paths, max distance annotated.
**Footer refs:** ABCB, *NCC 2022*, D1/D1.4. RMIT Brief (10% fire).

---

### Sheet 05 — Fire resistance & timber (Sec. C + B1)

**Narrative:** Structure must hold for escape. Class 3 + exposed timber = sprinklers + compartmentation + encapsulation/char design, not a Performance Solution loophole.
1. Compartment each storey
2. Sprinklers on Class 3 floors
3. FRL on structure + Class 3/6 separation
4. **Encapsulated or char-designed CLT/glulam** — sacrificial char layer sized into the panel, not full plasterboard boxing, to keep timber visible
5. RC podium at retail/transfer — naturally satisfies the separation

**Diagram:** Section — RC podium | timber tower | char layer callout | sprinkler zone.
**Footer refs:** ABCB, *NCC 2022*, Sec. C; Part B1. KLH *Multi-Story Residential*.

---

### Sheet 06 — How the materials are made

**Narrative:** **Concrete:** cement (limestone/clay kilned to ~1450°C) + aggregate + water, batched, poured in-situ or precast, cured ~28 days. **CLT:** kiln-dried boards layered at 90°, glued, pressed, then CNC-cut with openings pre-machined — arrives ready to lift, not to cut. **Glulam:** boards finger-jointed end-to-end, laminated all one grain direction, pressed straight or cambered/curved.

**Diagram:** Three-column process strip — concrete batching/pour, CLT layup/press/CNC, glulam finger-joint/lamination/press.
**Footer refs:** AT1.4 Structural System Report §3. APA Engineered Wood Association; XLam Australia (Wodonga plant).

---

### Sheet 07 — Forms and shapes

**Narrative:** **Concrete:** in-situ to any formwork shape, precast panels, post-tensioned slabs for longer podium spans, off-form finish from smooth to textured/board-marked. **CLT:** flat panels, ~2.4–3.0 m wide, up to ~16–18 m long, 3–7 ply (90–280 mm+). **Glulam:** straight, cambered, or curved beams/columns, built up from finger-jointed boards well beyond single-tree lengths.

**Diagram:** Sample forms — CLT panel with ply build-up callout, glulam straight/cambered/curved profiles, concrete off-form texture sample.
**Footer refs:** AT1.4 Structural System Report §4.

---

### Sheet 08 — Structural connections (the four 1:5 details)

**Narrative:** A hybrid is defined by its joints, not just its materials.
1. **Glulam column → steel base plate → RC pedestal**, with a moisture break — timber end grain never sits directly on damp concrete.
2. **CLT panel → glulam beam**, concealed steel connector let into the timber — no exposed brackets, keeps the soffit clean.
3. **CLT diaphragm → steel collector → RC core**, so lateral load has a continuous path into the shear walls.
4. **RC transfer beam/slab** at the podium-to-tower interface — also where the Class 6/3 fire separation is physically formed.

**Diagram:** Four numbered 1:5 connection details, callout to full section.
**Footer refs:** AT1.4 Structural System Report §5. Timber Fire Safety in Construction (connection detailing).

---

### Sheet 09 — Embodied energy comparison

**Narrative:** Concrete is low **per kilogram** (~0.36 kg CO₂e/kg) but dominates whole-building carbon because of the volume used in slabs, footings, cores. Steel is high per kilogram (structural steel ~3.9–4.3 kg CO₂e/kg). An Australian mid-rise study found mass timber buildings averaging ~417 kg CO₂e/m² against ~465 kg CO₂e/m² for an equivalent post-tensioned concrete building — roughly a 48 kg CO₂e/m² mean reduction; a separate Australian CLT-vs-RC comparison found ~30% GHG savings. **The honest claim is "substantially lower," not "carbon neutral"** — this hybrid still has a concrete podium/core.

**Diagram:** Bar chart — kg CO₂e/m² mass timber building vs. concrete building, plus per-kg comparison strip (concrete/steel/timber).
**Footer refs:** AT1.4 Structural System Report §6. Certified Energy, Australian material factors; Jayalath et al., CLT vs. RC Australian LCA.

---

### Sheet 10 — Span report: why this grid

**Narrative:** A 6.0 m floor span sits at the practical ceiling of a **7-ply CLT panel** before vibration governs (floor spans are almost always vibration-limited, not strength-limited) — not an arbitrary round number. Published cost-per-span data for glulam+CLT bays shows cost rising near-linearly with span for single spans, but a **cost-optimum near a ~7.3 m square bay with one secondary beam** — smaller grids with shorter beam spans are consistently cheaper because beam depth (timber volume) is minimised. **6.0 m stays inside CLT's efficient span range and the cheap end of the cost curve; 7.2 m matches the published cost-optimum bay size but trades some efficiency for planning flexibility.**

**Diagram:** Two charts — CLT span-by-ply table (3/5/7-ply, floor vs. roof), and cost-per-m² vs. grid-spacing curve with the optimum marked.
**Footer refs:** AT1.4 Structural System Report §10. *Structural Basics of Mass Timber* / *Structural Design with Mass Timber* (`resources/5-...` and `resources/6-...`).

---

### Sheet 11 — Mass timber acoustic detailing

**Narrative:** Mass timber is light, which makes it structurally efficient but **acoustically sensitive** — sound and vibration control are mass-driven. Baseline floor assembly: finish → topping screed → resilient mat → CLT panel, nothing hard-fixed underneath so the soffit stays exposed. Code-minimum airborne separation (STC 50) needs ~100 mm of buildup above the CLT; a higher-performance target (~STC 58) needs closer to 195 mm — **roughly double**, a real floor-to-floor height cost. **Flanking sound** around rigid CLT-to-CLT and CLT-to-glulam junctions is a known, still-researched limitation — party walls between studios need a deliberate acoustic break, not just panel thickness.

**Diagram:** Section through typical studio party wall + floor junction, annotated buildup and STC target.
**Footer refs:** AT1.4 Structural System Report §9. *Structural Design with Mass Timber* (`resources/6-...`); WoodWorks Mass Timber Fire & Acoustic Database. ABCB, *NCC 2022*, F7.

---

### Sheet 12 — F2/sanitary, wet areas, DDA-accessible studio

**Narrative:** Sanitary, waterproofing, accessible paths — especially DDA rooms.
- **F2:** ensuites in studios + communal WCs/basins per Tables F2.3/F2.4
- **10.2:** wet-area waterproofing (ensuite + communal)
- **AS 1428.1:** DDA 30–35 m², 1:20, ≥850 mm clear doors, turning circles

**Diagram:** DDA room plan + ensuite wet-area hatch, on the CLT/glulam grid established in Sheet 10.
**Footer refs:** ABCB, *NCC 2022*, F2; Part 10.2. AS 1428.1.

---

### Sheet 13 — How it's built: construction sequence

**Narrative:** Order matters. **(1)** Foundations + RC podium — conventional formwork/rebar/pour/cure, on the critical path. **(2)** RC core climbs ahead of the podium (jump-form) — it's both the lateral bracing and construction access. **(3)** Transfer slab/beams cast once podium concrete cures — where the retail grid resolves into the tighter residential grid, and where the Class 6/3 fire separation is physically formed. **(4)** Timber tower erects storey-by-storey ("platform construction") — pre-cut CLT/glulam craned in dry, largely without wet trades. **(5)** Envelope/fit-out follow close behind. **Net effect: podium speed is conventional; the tower above goes up substantially faster.**

**Diagram:** 5-step construction sequence strip, podium → core → transfer → timber erection → envelope.
**Footer refs:** AT1.4 Structural System Report §7.

---

### Sheet 14 — First Nations materials, suppliers, construction methods

**Narrative:** Procurement is a design decision, not a compliance add-on. **Supply Nation** certifies Aboriginal/Torres Strait Islander-owned businesses (≥51% owned/managed/controlled) — the practical first step for civil, joinery, and project-services trades on this project. **Precedents at scale:** the Tiwi Forestry Project (NT) — Indigenous-led commercial forestry funding community infrastructure; **Intract Indigenous Contractors** — 51% Indigenous-owned, delivering civil works today. **Honest gap:** no large-volume Indigenous-owned CLT/glulam mill currently supplies Victoria — the realistic response is Supply Nation-certified subcontractors wherever the chain allows, and genuine **Wurundjeri Woi-wurrung** engagement on material/landscape decisions from schematic design, not added after the structure is fixed. Carries into **AT3**.

**Diagram:** Procurement chain diagram — certified/Indigenous-owned trades marked at each stage from forestry to on-site delivery.
**Footer refs:** AT1.4 Structural System Report §8. Supply Nation; FWPA, *Indigenous Owned and Managed Forests*; National Indigenous Forestry Strategy.

---

### Sheet 15 — Precedents: proof it's buildable

**Narrative:** **Brock Commons Tallwood House** (UBC, Vancouver, 2017) — 18 storeys, RC core + glulam columns + CLT floors, erected in ~70 days once timber started, built as **student residence**. **La Trobe University Student Accommodation** (Bundoora, Melbourne) — 624 beds, JCB architects, largest mass timber project in Victoria by volume, 90%+ of loadbearing walls/columns in CLT/glulam, same Victorian CLT/glulam supply chain proposed here. **Together: Brock Commons proves the height, La Trobe proves it here, at this scale, with this supply chain.**

**Diagram:** Two precedent panels side by side — building photo/section placeholder, key stats, structural diagram callout for each.
**Footer refs:** AT1.4 Structural System Report §2. Acton Ostry Architects/UBC; Jackson Clements Burrows Architects.

---

### Sheet 16 — Whole-building summary

**Narrative:** Mixed **Class 3/Class 6**. Hybrid B — RC podium/core/transfer, CLT + glulam tower on a 6.0 m grid (7.2 m alternative) — is the **means** to meet the NCC on this site, not a separate design layer bolted onto it. Escape via dual stairs (D1); fire via sprinklers, compartments, podium separation, char-designed timber (Sec. C/B1); amenity via F2 + 10.2 + AS 1428.1 + acoustic buildup (F7); embodied energy substantially reduced vs. an all-concrete scheme, honestly stated; procurement carries First Nations engagement into AT3.

| Part | Response |
|---|---|
| A6 | Class 3 tower + Class 6 retail |
| D1 | Dual stairs, measured travel |
| C/B1 | RC podium; char-designed timber |
| F2/10.2/F7 | Ensuites + communal; waterproof; acoustic buildup |
| AS 1428.1 | DDA 1:20 |
| Structure | Hybrid B — RC podium/core + CLT/glulam tower |

**Diagram:** Full-building axonometric or long section, all systems labelled.
**Footer refs:** ABCB, *NCC 2022*, A6, C, B1, D1, F2, F7, 10.2. AS 1428.1. AT1.4 Structural System Report (full).

---

## Claude Design prompt (paste as-is)

```
Build an A3 landscape folio for RMIT AT1.4 Structural System Report — Week 2.
Repo: https://github.com/feangkan/AAT_Tools (branch cursor/aat-tools-resources-3c74)
Build spec: docs/AT1.4-week2-sheet-build-spec.md (16 sheets, content below)
Full research backing each sheet: docs/AT1.4-structural-system-report-final.md

Rules:
- A3 landscape, 420 x 297mm. Minimum 6 sheets — this set has 16; do not compress to force-fit a smaller count.
- Left = one diagram, right = ~80-120 word narrative, per sheet as specified.
- Yellow-highlight 1-2 key NCC/structural phrases per sheet.
- Chicago refs as a tiny footer on every sheet (no separate references page).
- Title block bottom-right: "63-67 Nicholson St, Footscray - ACZ1 - Wurundjeri Country - Sheet x/16"
- Follow the 16-sheet order exactly as written in the build spec.
- Pull diagram source images from resources/ PDFs and project-information/ where noted per sheet; draw hybrid sections/connection details fresh where no source image exists.
- Hybrid B (Mass Timber + Concrete) is locked — do not reintroduce Hybrid A/C as open options.
```

---

## Questions before this goes to Claude Design

1. **16 sheets is a lot — do you want it trimmed?** The brief only requires a minimum of 6. Candidates to merge if you want it shorter: Sheet 06 (material production) + Sheet 07 (forms/shapes) into one sheet; Sheet 09 (embodied energy) + Sheet 10 (span report) into one "performance data" sheet; Sheet 14 (First Nations) could sit right after Sheet 13 (construction) as a combined "procurement + construction" sheet. That would bring it to ~12–13 without dropping content, just density.
2. **Grid: 6.0 m or 7.2 m** — Section 10 deliberately left this open (6.0 m is cheaper/more efficient per the cost data, 7.2 m matches the published cost-optimum bay size and gives more planning flexibility). I need one number to draw the typical floor plan and section consistently across sheets 04, 12, and 16. Which do you want?
3. **Precedents (Sheet 15)** — one combined sheet or split into two full sheets (one each for Brock Commons and La Trobe), given you specifically asked for "more slides about precedent"? Two full sheets would let each carry its own structural diagram at proper size.
4. **Sheet order** — I put NCC classification first (01–05) then structure/materials (06–13), First Nations (14), precedents (15), summary (16). If you'd rather lead with the structural system and precedents (since that's the actual AT1.4 assessment focus) and push NCC classification later, I can reorder — tell me which reads better for your studio's expectations.

Once you confirm grid, sheet count, and precedent layout, I'll finalise this spec and it's ready to hand to Claude Design as-is.
