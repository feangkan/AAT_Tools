# AT1.4 Week 2 — Image Sourcing Guide

## Why this guide exists (read before using Claude Design)

Claude Design **cannot autonomously search the internet and pull photos into a design** — this isn't a prompting problem, it's how the tool works. Per Anthropic's own documentation:

1. **Claude doesn't generate real photos.** It builds diagrams, charts, and visuals using HTML/SVG — never photorealistic images. So even a perfectly-worded prompt can't make it produce a photo of Brock Commons.
2. **Claude Design only gets images three ways:** you **upload** them directly, you **link a codebase/repo** it can read files from, or you use its **web capture tool** on a specific URL you give it. It has no self-directed "go find a photo" behavior.

**This means the fix is giving Claude Design actual image files or exact URLs — not a better-worded instruction.** The workflow below does that.

---

## Workflow: how to actually get images into the Claude Design folio

**For the 5 real-building precedent sheets (02–07 except Monash's two-project sheet):**
1. I've sourced real candidate photos for each precedent below (with source links).
2. **Download them:** open each link, save the image to your computer.
3. **Upload to `resources/mass-timber-curated/images/`** in the GitHub repo (drag-and-drop upload via github.com — I can't fetch these into the repo myself, since my network access is restricted to a fixed allowlist that doesn't include image-hosting or architecture sites).
4. **When you start the Claude Design project, upload these images directly as reference material** (or use Claude Design's web capture tool pointed at the specific URLs below) — this is the only way Claude Design actually receives them.

**For technical/schematic diagrams (Sheets 01, 08–21):** these don't need real photos — they're diagrams Claude Design *can* build itself from a clear description, provided the description is specific (which the table below gives it). No image sourcing needed for these; just detailed instructions.

---

## Sheet-by-sheet image spec

| Sheet | Diagram template | Internal source (repo) | External source | Action needed |
|---|---|---|---|---|
| **01** — Hybrid B overview | Full-height section, RC podium/core/tower labelled | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (check for section diagrams) | — | Claude Design can draw this fresh from the description; no photo needed |
| **02** — Fenner Hall | Building photo + structural callout | — | [Fenner Hall — INDE.Awards](https://www.indeawards.com/) · [Make It Wood — Fenner Hall](https://makeitwood.org/) | Download photo, credit "Lendlease / Make It Wood" |
| **03** — La Trobe | Building photo + structural callout | — | [ArchitectureAU — JCB La Trobe accommodation](https://architectureau.com/) | Download photo, credit "Jackson Clements Burrows Architects" |
| **04** — Brock Commons | Building photo + structural callout | — | [Mercer Mass Timber — Brock Commons](https://mercermasstimber.com/) · [UBC Brock Commons](https://www.ubc.ca/) | Download photo, credit "Acton Ostry Architects / UBC" |
| **05** — Monash (Gillies Hall + Clayton) | Two-panel: built photo (Gillies Hall) + construction progress/render (Clayton) | — | [AECOM — Gillies Hall](https://aecom.com/projects/gillies-hall-student-accommodation-peninsula-campus-monash-university-victoria-australia/) · [Wood Central — Monash Clayton](https://woodcentral.com.au/monash-to-begin-work-on-new-hybrid-timber-student-residence/) | Download both, credit "Jackson Clements Burrows Architects" and "ADCO / Wood Central" respectively |
| **06** — Atlassian Central | Building photo + concrete/steel/timber zone callout | — | [New Atlas — Atlassian Central topped out](https://newatlas.com/architecture/atlassian-central-timber-tower-tops-out/) · [Dezeen — Atlassian Central](https://www.dezeen.com/2026/07/23/world-tallest-timber-tower-atlassian-central-sydney/) | Download photo, credit "SHoP Architects / BVN" — **must show the steel exoskeleton clearly, since the sheet's argument depends on it being visible** |
| **07** — 25 King Street | Facade elevation detail — diagonal bracing + ground colonnade | — | [Archdaily — 25 King Street Brisbane](https://www.archdaily.com/) · [Builtworks — 25 King St](https://builtworks.com.au/) | Download photo showing the diagonal bracing pattern specifically, credit "Bates Smart Architects" |
| **08** — Material production | 3-column process strip (concrete/CLT/glulam) | `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf`, `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` — check for process diagrams | [Stora Enso — CLT products](https://www.storaenso.com/en/products/mass-timber-construction/building-products/clt) (product/process imagery) | Check repo PDFs first; Claude Design can also draw this as a clean schematic strip from the written process description — no photo required |
| **09** — Forms/shapes | Product samples: CLT ply cross-section, glulam profiles, concrete texture | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` | XLam Australia, ASH Group product pages (optional, for real product photos) | Schematic redraw is fine — no strict photo requirement |
| **10** — Connections | Four numbered 1:5 details | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf`, `resources/klh-building-system-multi-story-residential-buildings.pdf` | [NACHI — lateral load connection](https://www.nachi.org/gallery/framing-2/lateral-load-connection) | Draw fresh — these are project-specific details, not sourced from elsewhere |
| **11** — Embodied energy | Bar chart, kg CO₂e/m² comparison | Data already in `docs/AT1.4-structural-system-report-final.md` §6 | — | Claude Design builds the chart directly from the data table in the sheet spec — no image needed |
| **12** — Span report | CLT span-by-ply chart + cost-vs-grid curve | `resources/5-MassTimberPedagogy-101-StructuralBasics.pdf` (span tables), `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (cost-span study) | — | Extract/redraw the tables directly from these two PDFs — they contain the source data |
| **13** — Acoustics | Section, party wall + floor junction | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (acoustic assembly section) | [WoodWorks Mass Timber Fire & Acoustic Database](https://www.woodworks.org/) | Draw fresh from the buildup data in the sheet spec |
| **14** — Construction sequence | 5-step strip, podium→core→transfer→timber→envelope | `resources/klh-building-system-multi-story-residential-buildings.pdf` | — | Draw fresh — project-specific sequence |
| **15** — First Nations | Procurement chain diagram | — | [Supply Nation](https://www.supplynation.com.au/), [FWPA — Indigenous forests report](https://www.fwpa.com.au/) | Draw fresh flowchart — no photo needed |
| **16** — NCC classification | Section, Class 6/Class 3 split | `resources/NCC 2015 PART-A3 CLASSIFICATION OF BUILDINGS AND STRUCTURES.pdf` | — | Draw fresh from classification data |
| **17** — Classification consequences | Flow diagram | — | — | Draw fresh |
| **18** — Escape D1 | Typical floor plan, 6.0 m grid | Project's own preliminary plans if available; otherwise draw schematic per brief numbers | — | Draw fresh per D1 requirements listed in sheet |
| **19** — Fire resistance | Section, char layer + sprinkler callout | `resources/6-MassTimberPedagogy-101-StructuralDesign.pdf` (fire-rated assembly) | — | Draw fresh |
| **20** — F2/DDA | DDA room plan, 6.0 m grid | Project's own preliminary plans if available | — | Draw fresh per AS 1428.1 requirements |
| **21** — Summary | Full-building axonometric, labelled | — | — | Draw fresh — this is the synthesis diagram, no source needed |

---

## Precedent photo links (direct — for downloading now)

These are the specific images I located for the five real-building precedent sheets. Open each, save the image, and follow the upload workflow above.

- **Fenner Hall:** https://www.indeawards.com/ (search "Fenner Hall") · https://makeitwood.org/
- **La Trobe:** search "Jackson Clements Burrows La Trobe student accommodation" on architectureau.com
- **Brock Commons:** https://mercermasstimber.com/ (search "Brock Commons Tallwood House")
- **Monash — Gillies Hall:** https://aecom.com/projects/gillies-hall-student-accommodation-peninsula-campus-monash-university-victoria-australia/
- **Monash — Clayton (under construction):** https://woodcentral.com.au/monash-to-begin-work-on-new-hybrid-timber-student-residence/
- **Atlassian Central:** https://newatlas.com/architecture/atlassian-central-timber-tower-tops-out/ · https://www.dezeen.com/2026/07/23/world-tallest-timber-tower-atlassian-central-sydney/
- **25 King Street:** search "25 King Street Brisbane" on archdaily.com or builtworks.com.au

**Note on copyright:** these are professional architecture photos, typically credited to the architect/photographer on the source page. Use them for this coursework with attribution (as the sheet spec already requires in its Footer refs), and don't strip or omit the credit line when uploading.

---

## Updated Claude Design prompt (paste as-is)

```
Build an A3 landscape folio for RMIT AT1.4 Structural System Report — Week 2.
Repo: https://github.com/feangkan/AAT_Tools (branch cursor/aat-tools-resources-3c74)
Build spec: docs/AT1.4-week2-sheet-build-spec.md (21 sheets, content below)
Image sourcing guide: docs/AT1.4-week2-image-sourcing-guide.md
Full research backing each sheet: docs/AT1.4-structural-system-report-final.md

I am uploading reference photos for Sheets 02-07 (precedent buildings) directly to this project —
use these uploaded images for those sheets, cropped/placed as needed, with the credit line shown
in the image sourcing guide table. Do not attempt to fetch or invent photos for these sheets;
use only the uploaded reference images.

For Sheets 01, 08-21 (technical/schematic diagrams): build these directly as clean vector diagrams
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
- Precedent order (Sheets 02-07) is deliberate — do not reorder by height or fame.
- Sheet 06 (Atlassian) must show the steel exoskeleton visibly and state clearly it's not an identical Hybrid B match.
```
