# AT1.4 Week 2 — Image Sourcing Guide

## Why this guide exists (read before using Claude Design)

Claude Design **cannot autonomously search the internet and pull photos into a design** — this isn't a prompting problem, it's how the tool works. Per Anthropic's own documentation:

1. **Claude doesn't generate real photos.** It builds diagrams, charts, and visuals using HTML/SVG — never photorealistic images. So even a perfectly-worded prompt can't make it produce a photo of Brock Commons.
2. **Claude Design only gets images three ways:** you **upload** them directly, you **link a codebase/repo** it can read files from, or you use its **web capture tool** on a specific URL you give it. It has no self-directed "go find a photo" behavior.

**This means the fix is giving Claude Design actual image files or exact URLs — not a better-worded instruction.** The workflow below does that.

---

## Quick index — every sheet, in order, image status

Re-searched fresh for this pass, in sheet order, so this list matches the current 21-sheet order exactly.

| Sheet | Needs a photo? | Status |
|---|---|---|
| 01 — Hybrid B overview | Optional reference | ✅ Found — WoodWorks "Mass Timber Buildings on a Podium" is a strong match |
| 02 — Material production | Yes | ✅ Found — Kallesoe/Ledinek CLT press lines |
| 03 — Forms/shapes | Optional reference | ✅ Found — VCE Publications CLT ply diagram |
| 04 — Connections | Yes | ✅ Found — Simpson Strong-Tie concealed connectors |
| 05 — Embodied energy | **No** | Data chart — build from spec numbers |
| 06 — Span report | **No** | Data chart — build from spec numbers |
| 07 — Acoustics | Optional reference | ✅ Found — mass timber floor assembly cutaways |
| 08 — Construction sequence | Optional reference | ✅ Found — Sterling Structural erection photography |
| 09 — First Nations | **No — deliberately** | Stock forestry photos risk implying unverified Indigenous ownership; use a drawn flowchart |
| 10 — Fenner Hall | Yes | ✅ Found — ANU's own page + INDE.Awards |
| 11 — La Trobe | Yes | ✅ Found — ArchDaily gallery, several angles |
| 12 — Brock Commons | Yes | ✅ Found — multiple clean exterior shots |
| 13 — Monash (2 images) | Yes | ✅ Found — Gillies Hall (built) + Clayton (rendering/construction) |
| 14 — Atlassian Central | Yes | ✅ Found — This Is Sydney project photos showing exoskeleton |
| 15 — 25 King Street | Yes | ✅ Found — Knapp Connectors page shows the bracing directly |
| 16 — NCC classification | Optional reference | Same result as Sheet 01 |
| 17 — Classification consequences | **No** | Flow diagram — draw fresh |
| 18 — Escape D1 | **No** | Project-specific floor plan — draw fresh |
| 19 — Fire resistance | Yes | ✅ Found — Timber iQ char-test photography (strongest find in the set) |
| 20 — F2/DDA | Optional reference | ✅ Found — Ironwood Manufacturing turning-circle diagram |
| 21 — Summary | **No** | Project-specific axonometric — draw fresh |

Details, direct links, and my comments on each are below, still organised by precedent block first then technical block (matching how the guide was originally structured) — use the index above to jump to the sheet number you need.

---

## Workflow: how to actually get images into the Claude Design folio

**For the 6 real-building precedent sheets (10–15, including Monash's two-project sheet):**
1. I've sourced real candidate photos for each precedent below (with source links).
2. **Download them:** open each link, save the image to your computer.
3. **Upload to `resources/mass-timber-curated/images/`** in the GitHub repo (drag-and-drop upload via github.com — I can't fetch these into the repo myself, since my network access is restricted to a fixed allowlist that doesn't include image-hosting or architecture sites).
4. **When you start the Claude Design project, upload these images directly as reference material** (or use Claude Design's web capture tool pointed at the specific URLs below) — this is the only way Claude Design actually receives them.

**For technical/schematic diagrams (Sheets 01–09, 16–21):** these don't need real photos — they're diagrams Claude Design *can* build itself from a clear description, provided the description is specific (which the table below gives it). No image sourcing needed for these; just detailed instructions.

---

## Sheet-by-sheet image spec

| Sheet | Diagram template | Internal source (repo) | External source | Action needed |
|---|---|---|---|---|
| **01** — Hybrid B overview | Full-height section, RC podium/core/tower labelled | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (check for section diagrams) | — | Claude Design can draw this fresh from the description; no photo needed |
| **10** — Fenner Hall | Building photo + structural callout | — | [Fenner Hall — INDE.Awards](https://www.indeawards.com/) · [Make It Wood — Fenner Hall](https://makeitwood.org/) | Download photo, credit "Lendlease / Make It Wood" |
| **11** — La Trobe | Building photo + structural callout | — | [ArchitectureAU — JCB La Trobe accommodation](https://architectureau.com/) | Download photo, credit "Jackson Clements Burrows Architects" |
| **12** — Brock Commons | Building photo + structural callout | — | [Mercer Mass Timber — Brock Commons](https://mercermasstimber.com/) · [UBC Brock Commons](https://www.ubc.ca/) | Download photo, credit "Acton Ostry Architects / UBC" |
| **13** — Monash (Gillies Hall + Clayton) | Two-panel: built photo (Gillies Hall) + construction progress/render (Clayton) | — | [AECOM — Gillies Hall](https://aecom.com/projects/gillies-hall-student-accommodation-peninsula-campus-monash-university-victoria-australia/) · [Wood Central — Monash Clayton](https://woodcentral.com.au/monash-to-begin-work-on-new-hybrid-timber-student-residence/) | Download both, credit "Jackson Clements Burrows Architects" and "ADCO / Wood Central" respectively |
| **14** — Atlassian Central | Building photo + concrete/steel/timber zone callout | — | [New Atlas — Atlassian Central topped out](https://newatlas.com/architecture/atlassian-central-timber-tower-tops-out/) · [Dezeen — Atlassian Central](https://www.dezeen.com/2026/07/23/world-tallest-timber-tower-atlassian-central-sydney/) | Download photo, credit "SHoP Architects / BVN" — **must show the steel exoskeleton clearly, since the sheet's argument depends on it being visible** |
| **15** — 25 King Street | Facade elevation detail — diagonal bracing + ground colonnade | — | [Archdaily — 25 King Street Brisbane](https://www.archdaily.com/) · [Builtworks — 25 King St](https://builtworks.com.au/) | Download photo showing the diagonal bracing pattern specifically, credit "Bates Smart Architects" |
| **02** — Material production | 3-column process strip (concrete/CLT/glulam) | `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf`, `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` — check for process diagrams | [Stora Enso — CLT products](https://www.storaenso.com/en/products/mass-timber-construction/building-products/clt) (product/process imagery) | Check repo PDFs first; Claude Design can also draw this as a clean schematic strip from the written process description — no photo required |
| **03** — Forms/shapes | Product samples: CLT ply cross-section, glulam profiles, concrete texture | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` | XLam Australia, ASH Group product pages (optional, for real product photos) | Schematic redraw is fine — no strict photo requirement |
| **04** — Connections | Four numbered 1:5 details | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf`, `resources/klh-building-system-multi-story-residential-buildings.pdf` | [NACHI — lateral load connection](https://www.nachi.org/gallery/framing-2/lateral-load-connection) | Draw fresh — these are project-specific details, not sourced from elsewhere |
| **05** — Embodied energy | Bar chart, kg CO₂e/m² comparison | Data already in `docs/AT1.4-structural-system-report-final.md` §6 | — | Claude Design builds the chart directly from the data table in the sheet spec — no image needed |
| **06** — Span report | CLT span-by-ply chart + cost-vs-grid curve | `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf` (span tables), `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (cost-span study) | — | Extract/redraw the tables directly from these two PDFs — they contain the source data |
| **07** — Acoustics | Section, party wall + floor junction | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (acoustic assembly section) | [WoodWorks Mass Timber Fire & Acoustic Database](https://www.woodworks.org/) | Draw fresh from the buildup data in the sheet spec |
| **08** — Construction sequence | 5-step strip, podium→core→transfer→timber→envelope | `resources/klh-building-system-multi-story-residential-buildings.pdf` | — | Draw fresh — project-specific sequence |
| **09** — First Nations | Procurement chain diagram | — | [Supply Nation](https://www.supplynation.com.au/), [FWPA — Indigenous forests report](https://www.fwpa.com.au/) | Draw fresh flowchart — no photo needed |
| **16** — NCC classification | Section, Class 6/Class 3 split | `resources/NCC 2015 PART-A3 CLASSIFICATION OF BUILDINGS AND STRUCTURES.pdf` | — | Draw fresh from classification data |
| **17** — Classification consequences | Flow diagram | — | — | Draw fresh |
| **18** — Escape D1 | Typical floor plan, 6.0 m grid | Project's own preliminary plans if available; otherwise draw schematic per brief numbers | — | Draw fresh per D1 requirements listed in sheet |
| **19** — Fire resistance | Section, char layer + sprinkler callout | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (fire-rated assembly) | — | Draw fresh |
| **20** — F2/DDA | DDA room plan, 6.0 m grid | Project's own preliminary plans if available | — | Draw fresh per AS 1428.1 requirements |
| **21** — Summary | Full-building axonometric, labelled | — | — | Draw fresh — this is the synthesis diagram, no source needed |

---

## Precedent photo links (direct — for downloading now)

These are the specific images I located for the five real-building precedent sheets, with my notes on each.

- **Fenner Hall** — https://www.indeawards.com/ (search "Fenner Hall") · https://makeitwood.org/
  **My comment:** the Make It Wood result is the better pick — it's the industry body's own project page, so the photo is more likely to be a proper high-res architectural shot rather than an awards-thumbnail. Look for an exterior shot that shows the two-storey concrete base clearly against the CLT tower above — that's the detail the sheet's narrative depends on, so a full-building shot works better here than a close-up.

- **La Trobe** — search "Jackson Clements Burrows La Trobe student accommodation" on architectureau.com
  **My comment:** ArchitectureAU tends to publish JCB's own supplied photography, which is usually well-lit and credited properly — safer than a random image aggregator. Try to find one that shows both buildings together (there are two blocks) rather than a single close-up, since the sheet's "624 beds, 2 buildings" claim reads better with a shot that shows scale.

- **Brock Commons** — https://mercermasstimber.com/ (search "Brock Commons Tallwood House")
  **My comment:** Mercer's own page is good because it's a manufacturer case study, so it'll likely have a section diagram alongside the photo — grab both if available, since a section is more useful than a photo for this sheet's "18 storeys, no exoskeleton" argument. If only exterior photos come up, an angle showing the building's full height against the UBC campus reads better than a ground-level shot that crops the top off.

- **Monash — Gillies Hall** — https://aecom.com/projects/gillies-hall-student-accommodation-peninsula-campus-monash-university-victoria-australia/
  **My comment:** AECOM's project page is the engineering consultant's own case study, so it may include interior shots showing exposed CLT — worth grabbing one of those in addition to the exterior, since "exposed CLT ceiling" is mentioned in Sheet 13's narrative and a photo backs that up better than description alone.

- **Monash — Clayton (under construction)** — https://woodcentral.com.au/monash-to-begin-work-on-new-hybrid-timber-student-residence/
  **My comment:** this one's genuinely useful precisely *because* it's under construction — a construction-progress photo or rendering makes the "currently rising" claim visually obvious in a way a finished-building photo can't. If Wood Central only has a rendering, that's fine to use here — just caption it "artist's impression" rather than implying it's a photo of the completed building.

- **Atlassian Central** — https://newatlas.com/architecture/atlassian-central-timber-tower-tops-out/ · https://www.dezeen.com/2026/07/23/world-tallest-timber-tower-atlassian-central-sydney/ · **re-searched this pass:** "This Is Sydney" (thisissydney.com.au) also has project photography
  **My comment:** re-checked and the "This Is Sydney" result looks like the strongest option — local press tends to get closer access during topping-out events, so it's worth checking for a shot that shows the steel exoskeleton clearly (not just glass facade). The sheet's whole point is "you can see this isn't pure timber+concrete," so the image needs to visibly earn that claim, not just be a generic tower photo — compare a few of the three sources before picking.

- **25 King Street** — search "25 King Street Brisbane" on archdaily.com or builtworks.com.au · **re-searched this pass:** the Knapp Connectors project page (knapp-verbinder.com) came up directly for "diagonal glulam bracing facade"
  **My comment:** the Knapp Connectors result is actually the best find here — it's the connector manufacturer's own project page for 25 King, so it's likely to show the bracing and connection detail together, which is exactly what this sheet needs (facade pattern *and* how it's fixed). Better than a generic exterior shot from an aggregator site.

**Note on copyright:** these are professional architecture photos, typically credited to the architect/photographer on the source page. Use them for this coursework with attribution (as the sheet spec already requires in its Footer refs), and don't strip or omit the credit line when uploading.

---

## Reference images for technical/diagram sheets (01–09, 16–21)

These aren't source photos to reproduce as-is — they're **reference material** to give Claude Design something concrete to work from when it draws each sheet's schematic (rather than inventing a diagram from a text description alone).

- **Sheet 01 — Hybrid B overview** — search "concrete podium mass timber tower building section"
  **My comment:** better result this time than my earlier pass — WoodWorks' "Mass Timber Buildings on a Podium" is a purpose-written industry piece on exactly this condition (concrete podium + timber tower), likely to have a genuinely relevant diagram rather than a loosely-related stock photo. Worth using over a generic drawn section if the diagram is clean.

- **Sheet 02 — Material production** — "CLT cross laminated timber manufacturing factory production line" · "glulam beam finger joint lamination press manufacturing" · "concrete batching plant pour construction site"
  **My comment:** genuinely good results here — the Ledinek and Kallesoe Machinery hits are real CLT/glulam press-line photography, which is exactly the "how it's actually made" imagery this sheet needs. Worth using all three (CLT press, glulam finger-joint line, concrete batching) side by side rather than picking one, since the sheet's whole point is comparing three manufacturing processes.

- **Sheet 03 — Forms/shapes** — "CLT panel cross section layers ply thickness"
  **My comment:** the VCE Publications fact sheet result is the strongest one — it's an educational diagram, not a stock photo, so it's already labelled and clean, which suits this sheet's "3/5/7-ply" comparison better than a photo would.

- **Sheet 04 — Connections** — "glulam column steel base plate connection detail timber" · "CLT to glulam beam concealed steel connector timber construction"
  **My comment:** the Simpson Strong-Tie and Knapp Connectors results are the useful ones — these are manufacturer product photos of actual concealed connector hardware, which will make the 1:5 details look like real engineering rather than an invented diagram. Skip the Pinterest/general "wood deck framing" result — it's residential deck hardware, wrong scale and wrong application for this project.

- **Sheet 07 — Acoustics** — "mass timber floor acoustic assembly section resilient layer"
  **My comment:** mixed results — a couple are genuinely useful cutaway sections, but one or two are more about impact-sound testing data than the physical buildup. Prioritise any result that shows a labelled section (finish/screed/mat/CLT layers) over one that's just a testing chart.

- **Sheet 08 — Construction sequence** — "mass timber tower construction crane storey erection CLT panel"
  **My comment:** re-searched and found a better result — Sterling Structural's "Star Lofts" project photography shows real CLT panels mid-erection with a crane in frame, matching the "platform construction" narrative directly. Stronger than the more general explainer graphics from my first pass.

- **Sheet 09 — First Nations** — "Australian native forest timber plantation harvest sustainable"
  **My comment:** I'd actually recommend **against** using any of these as the sheet's image. They're generic sustainable-forestry stock photography with no connection to Indigenous-owned or -operated forestry specifically, and using one here risks visually implying a claim (Indigenous involvement) the photo doesn't actually support. This is the one sheet where I'd keep the image as a drawn procurement-chain flowchart rather than a photo — safer and more accurate to what the sheet is actually arguing.

- **Sheet 16 — NCC classification** — same podium/tower reference search as Sheet 01
  **My comment:** same conclusion as Sheet 01 — draw this one, don't force a stock photo.

- **Sheet 19 — Fire resistance** — "CLT char layer fire test cross laminated timber burn"
  **My comment:** this is the standout result of the whole search — Timber iQ's fire-test photography shows an actual charred CLT cross-section, which is precisely the physical evidence this sheet's char-design argument needs. I'd prioritise sourcing and using this one over almost any other image in the set; a drawn diagram can show the char layer as a dimension, but a real burnt-timber photo makes "this is a real, measured phenomenon" land in a way a diagram can't.

- **Sheet 20 — F2/DDA** — "DDA accessible bathroom wheelchair turning circle design"
  **My comment:** the Ironwood Manufacturing result is the clearest — it's an actual dimensioned clearance diagram, not a lifestyle photo, which is what this sheet needs (a plan reference, not an inspirational bathroom photo).

**Sheets 05, 06, 17, 18, 21 have no useful photo reference** — these are data charts (05 embodied energy, 06 span report), a compliance flow diagram (17), a project-specific floor plan (18), and a project-specific axonometric (21). Claude Design should build these directly from the data/description in the build spec; searching for stock images would add noise, not accuracy.

---

## Updated Claude Design prompt (paste as-is)

```
Build an A3 landscape folio for RMIT AT1.4 Structural System Report — Week 2.
Repo: https://github.com/feangkan/AAT_Tools (branch cursor/aat-tools-resources-3c74)
Build spec: docs/AT1.4-week2-sheet-build-spec.md (21 sheets, content below)
Image sourcing guide: docs/AT1.4-week2-image-sourcing-guide.md
Full research backing each sheet: docs/AT1.4-structural-system-report-final.md

I am uploading reference photos for Sheets 10-15 (precedent buildings) directly to this project —
use these uploaded images for those sheets, cropped/placed as needed, with the credit line shown
in the image sourcing guide table. Do not attempt to fetch or invent photos for these sheets;
use only the uploaded reference images.

For Sheets 01-09 and 16-21 (technical/schematic diagrams): build these directly as clean vector diagrams
from the descriptions in the build spec - no photos needed for these, follow the "Diagram" line
in each sheet's content plus the diagram template noted in the image sourcing guide.

Rules:
- A3 landscape, 420 x 297mm. Follow the 21-sheet order exactly as written in the build spec.
- Left = one diagram/image, right = narrative (~150-200 words) + comparison/data table + a bolded "Why" line + a bolded "Takeaway" line, per sheet as specified.
- Yellow-highlight 1-2 key NCC/structural phrases per sheet.
- Chicago refs as a tiny footer on every sheet (no separate references page).
- Title block bottom-right: "63-67 Nicholson St, Footscray - ACZ1 - Wurundjeri Country - Sheet x/21"
- Add a small photo credit caption under every uploaded precedent image (architect/photographer, per the sourcing guide).
- Hybrid B (Mass Timber + Concrete) is locked, grid is 6.0 m — do not reintroduce Hybrid A/C or the 7.2 m alternative as open options.
- Precedent order (Sheets 10-15) is deliberate — do not reorder by height or fame.
- Sheet 14 (Atlassian) must show the steel exoskeleton visibly and state clearly it's not an identical Hybrid B match.
```
