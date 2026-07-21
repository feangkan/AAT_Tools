# AT1.4 Claude Design Handoff — NCC-led 6× A3 Folio

Use this document as the **single brief** for Claude (or Canva/InDesign) to build the Week 2 **Structural System Report** on the AAT template.

**Project:** 63–67 Nicholson St, Footscray · RMIT ARCH3372 · Student accommodation + retail  
**Deliverable:** AT1.4 · **6× A3 landscape** · ~**70% NCC** · compact functional narrative  
**Classification:** **Class 3** residential + **Class 6** retail  

---

## 1. Main repo (clone or browse)

| Item | Link |
|------|------|
| **Repository** | https://github.com/feangkan/AAT_Tools |
| **Working branch** | https://github.com/feangkan/AAT_Tools/tree/cursor/aat-tools-resources-3c74 |
| **Draft PR** | https://github.com/feangkan/AAT_Tools/pull/1 |
| **This handoff file** | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/docs/AT1.4-claude-design-handoff.md |

```bash
git clone https://github.com/feangkan/AAT_Tools.git
cd AAT_Tools
git checkout cursor/aat-tools-resources-3c74
```

---

## 2. Where to pull pictures & content from (repo)

### Course brief & assessment PDFs (primary text source)

| Content | Repo path | GitHub link |
|---------|-----------|-------------|
| Project brief | `project-information/AAT_project_brief.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/project-information/AAT_project_brief.pdf |
| AT1 tasks (incl. AT1.4) | `assessment-tasks/Assessment Task 1_ Schematic Design.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/assessment-tasks/Assessment%20Task%201_%20Schematic%20Design.pdf |
| AT2 (NCC report scope) | `assessment-tasks/Assessment Task 2_ Design Development.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/assessment-tasks/Assessment%20Task%202_%20Design%20Development.pdf |
| Syllabus | `project-information/Syllabus for Architecture Advanced Technology (2650).pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/project-information/Syllabus%20for%20Architecture%20Advanced%20Technology%20(2650).pdf |

### NCC reference PDFs (clause screenshots / highlights)

| Topic | Repo path | GitHub link |
|-------|-----------|-------------|
| **A3/A6 Classification** | `resources/NCC 2015 PART-A3 CLASSIFICATION OF BUILDINGS AND STRUCTURES.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/NCC%202015%20PART-A3%20CLASSIFICATION%20OF%20BUILDINGS%20AND%20STRUCTURES.pdf |
| NCC 2019 Vol 1 (full) | `resources/NCC_2019_Volume_One_Amendment 1.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/NCC_2019_Volume_One_Amendment%201.pdf |
| **D1 Escape** | `resources/D1 Provision For Escape.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/D1%20Provision%20For%20Escape.pdf |
| **F2 Sanitary** | `resources/Part F2 Sanitary and Other Facilities.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/Part%20F2%20Sanitary%20and%20Other%20Facilities.pdf |
| Clause 58 / BADS | `resources/Apartment-Design-Guidelines-for-Victoria.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/Apartment-Design-Guidelines-for-Victoria.pdf |
| LHD | `resources/Livable-Housing-Design-Standard-2022-1.3.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/Livable-Housing-Design-Standard-2022-1.3.pdf |

> **Note:** For citations in folio, prefer **NCC 2022 online** (current edition): https://ncc.abcb.gov.au/ — repo NCC PDFs are for screenshots only.

### Mass timber / structure images (precedents & diagrams)

| Content | Repo path | GitHub link |
|---------|-----------|-------------|
| Mass timber basics (61 pp — CLT, glulam, systems) | `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/5-MassTimberPedagogy-101-StructuralBasics.pdf |
| Mass timber design | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/6-MassTimberPedagogy-101-StructuralDesign.pdf |
| KLH multi-storey residential | `resources/klh-building-system-multi-story-residential-buildings.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/klh-building-system-multi-story-residential-buildings.pdf |
| KLH residential EN | `resources/klh-residential-en.pdf` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/resources/klh-residential-en.pdf |

**Suggested PDF pages to export as images for folio:**

| Sheet | Pull from | Pages (approx.) |
|-------|-----------|-----------------|
| 02 | Mass Timber Module 1 | Hybrid systems ~p.29–30; bearing wall ~p.26 |
| 04 | KLH multi-storey | System diagrams, connections |
| 04 | Mass Timber Module 1 | CLT section ~p.14; post-and-beam ~p.28 |
| 01 | NCC A3 PDF | Class 3 definitions (A6G4) |
| 03 | D1 PDF | Travel distance / exit diagrams |

### Machine-readable brief & rules (for accurate numbers)

| File | Purpose | Link |
|------|---------|------|
| `data/brief/project_brief.json` | Units, classes, communal areas, deliverables | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/data/brief/project_brief.json |
| `data/rules/compliance_rules.json` | NCC/BADS checks (D1 travel 40 m, etc.) | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/data/rules/compliance_rules.json |
| `data/knowledge/curated_excerpts.json` | Searchable course + NCC summaries | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/data/knowledge/curated_excerpts.json |

---

## 3. A3 template reference (layout, not final export)

| Item | Path | Link |
|------|------|------|
| Web A3 sheet component | `frontend/src/components/A3Preview.tsx` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/frontend/src/components/A3Preview.tsx |
| PDF export engine | `backend/app/services/a3_export.py` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/backend/app/services/a3_export.py |
| Structure options copy | `backend/app/services/details.py` | https://github.com/feangkan/AAT_Tools/blob/cursor/aat-tools-resources-3c74/backend/app/services/details.py |

**Template specs:** A3 **landscape** · 420 × 297 mm · title block bottom-right · site line “63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country” · sheet x/6.

---

## 4. External images (only if not in repo PDFs)

| Need | Source |
|------|--------|
| NCC A6G4 Class 3 clause (current) | https://ncc.abcb.gov.au/ → Vol. 1 → Part A6 |
| Brock Commons Tallwood House | Acton Ostry / UBC (project photos — credit architect) |
| ABCB classification explainer | https://abcb.gov.au/ncc-navigator/building-classifications |
| Vic planning Clause 58 | https://www.planning.vic.gov.au/guides-and-resources/guides/all-guides/residential-development/apartment-developments |
| Footscray / Nicholson St context | Google Maps / Vicmap (attribute sources) |

---

## 5. Design order — 6 sheets (copy to Claude)

**Rules:** Left = one diagram. Right = short narrative (~80–120 words). Yellow-highlight 1–2 NCC phrases. **Refs as tiny footer on each sheet** (Chicago, not separate page). ~70% NCC.

---

### Sheet 01 — What is this building under the NCC?

**Narrative:** Classification follows **use**. Mixed building: **Class 3** student lodging above **Class 6** retail.

- **Class 3 (A6G4):** Long-term or transient accommodation for unrelated persons; hostel / lodging house.
- **Evidence:** Communal kitchen 120–150 m²; studios 15–25 m² ensuite; shared laundry, gym, study — managed student accommodation.
- **Class 6:** Ground retail.
- **A6G1:** Each part classified separately; Class 3 + Class 6 permitted.

**Diagram:** Section — Class 6 podium | Class 3 tower | fire separation line.

**Footer refs:** ABCB, *NCC 2022*, Vol. 1, A6G1, A6G4. RMIT, *AAT Project Brief*.

**Images:** NCC A3 PDF classification page; brief p.1–2.

---

### Sheet 02 — Classification consequences

**Narrative:** Class 3 accommodation serves unrelated occupants in a managed building — fire and egress requirements reflect that use.

| NCC issue | Consequence |
|-----------|-------------|
| Fire separation | Rated separation Class 6 ↔ Class 3 |
| Sprinklers | Class 3, 2+ storeys → sprinklers throughout residential floors |
| D1 | Min 2 fire-isolated exits |
| 2.1 / C | Structure + FRL support fire strategy |
| AS 1428.1 | DDA 1:20 on Class 3 floors |

**Outcome:** RC podium + timber tower only if fire strategy shown.

**Diagram:** Class 3 → sprinklers + dual stairs + podium fire wall → hybrid structure.

**Footer refs:** ABCB, *NCC 2022*, A6G4; Sec. C; D1.

---

### Sheet 03 — Escape (D1)

**Narrative:** Plan organised for escape before fire spread. ~20 rooms/floor → **two fire-isolated stairs**.

- ≥ 2 exits · travel ≤ ~40 m · dead-end ≤ ~20 m · exit width ≥ 1000 mm · corridor 1.8–2.0 m
- Brief **10%** fire/duct allowance in cores/shafts

**Diagram:** Typical floor — core, 2 stairs, dashed travel paths, max distance annotated.

**Footer refs:** ABCB, *NCC 2022*, D1/D1.4. RMIT Brief (10% fire).

---

### Sheet 04 — Fire resistance & timber (C + 2.1)

**Narrative:** Structure must hold for escape. Class 3 + timber = sprinklers + compartmentation + encapsulation or Performance Solution.

1. Compartment each storey  
2. Sprinklers Class 3 floors  
3. FRL on structure + Class 3/6 separation  
4. Encapsulated CLT/glulam or fire-engineered char  
5. RC podium at retail/transfer  

**Diagram:** Section — RC podium | timber tower | gypsum encapsulation | sprinkler zone.

**Footer refs:** ABCB, *NCC 2022*, Sec. C; Part 2.1. KLH *Multi-Story Residential*.

---

### Sheet 05 — F2, wet areas, access

**Narrative:** Sanitary, waterproofing, accessible paths — especially DDA rooms.

- **F2:** Ensuites in studios + communal WCs/basins per Tables F2.3/F2.4  
- **10.2:** Wet-area waterproofing (ensuite + communal)  
- **AS 1428.1:** DDA 30–35 m², 1:20, ≥850 mm clear doors, turning circles  

**Diagram:** DDA room plan + ensuite wet-area hatch.

**Footer refs:** ABCB, *NCC 2022*, F2; Part 10.2. AS 1428.1.

---

### Sheet 06 — Whole-building NCC summary

**Narrative:** Mixed **Class 3 / Class 6**. Class 3 managed student lodging with shared kitchen and communal facilities. Escape via dual stairs under D1. Fire via sprinklers, compartments, podium separation, protected timber. Amenity via F2 + 10.2 + AS 1428.1. Hybrid structure is the **means** to meet NCC on this site.

| Part | Response |
|------|----------|
| A6 | Class 3 tower + Class 6 retail |
| D1 | Dual stairs, measured travel |
| C / 2.1 | RC podium; encapsulated timber |
| F2 / 10.2 | Ensuites + communal; waterproof |
| AS 1428.1 | DDA 1:20 |

**Footer refs:** ABCB, *NCC 2022*, A6, C, D1, F2, 2.1, 10.2. AS 1428.1. RMIT Brief.

---

## 6. Claude prompt (paste as-is)

```
Build 6× A3 landscape folio pages for RMIT AT1.4 Structural System Report.

Repo: https://github.com/feangkan/AAT_Tools (branch cursor/aat-tools-resources-3c74)
Handoff: docs/AT1.4-claude-design-handoff.md

Rules:
- ~70% NCC content; structure only where it serves compliance
- Class 3 residential + Class 6 retail
- Do not discuss or compare other building classes — state Class 3 positively only
- Compact functional narrative; 80–120 words body per sheet
- One diagram left, text right; yellow NCC highlights
- Chicago refs as tiny footer each sheet (no separate refs page)
- Pull images from repo PDFs (resources/, project-information/, assessment-tasks/)
- Use NCC 2022 online for current clause wording if repo PDF is older

Follow sheet order 01–06 in the handoff doc exactly.
Site: 63–67 Nicholson St, Footscray. Format: A3 landscape. 6 pages minimum.
```

---

## 7. Key numbers (from brief)

| Item | Value |
|------|-------|
| Studios | 200+ · 15–25 m² |
| DDA | 1 per 20/floor · 30–35 m² · Class 3 |
| FTC | ≥ 2.7 m |
| Communal kitchen | 120–150 m² |
| Services allowance | 5% |
| Fire/duct allowance | 10% |
| Retail | Class 6 ground |
| Zone | ACZ1 Footscray |

---

*Generated for AAT Studio Tools · ARCH3372 · Week 2 AT1.4*
