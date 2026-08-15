# AT2 → Claude Design

This file is a **production brief for Claude Design**, not the student folio. Tutors should not be shown this file.

**Student-facing copy (source of truth — paste/layout from these, do not rewrite):**

| Folio | File | Sheets |
|---|---|---|
| AT2.1 NCC | [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) | 12 |
| AT2.2 LHD + BADS | [`docs/AT2.2-lhd-bads-report.md`](./AT2.2-lhd-bads-report.md) | 16 |
| AT2.3 Energy | [`docs/AT2.3-environmental-report.md`](./AT2.3-environmental-report.md) | 12 |

**Repo / branch to connect in Claude Design**

- Repo: https://github.com/feangkan/AAT_Tools
- Branch: `cursor/at2-week5-f836`
- AT2.1: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.1-week5-NCC-report.md
- AT2.2: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.2-lhd-bads-report.md
- AT2.3: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.3-environmental-report.md

Start at https://claude.ai/design · connect this GitHub repo on that branch · paste **the single prompt below** (one project, one 40-sheet PDF).

---

## Layout (all AT2 sheets)

These are **text slides**, not the AT1.4 half-diagram / half-text layout.

A3 landscape **420 × 297 mm**. Navy `#1f4b66`, white ground, black hairline border inset ~8 mm.

| Zone | What goes there |
|---|---|
| Header | `ARCH3372 · AT2.x · 63–67 Nicholson St, Footscray` · sheet title from the markdown `## N. …` heading |
| Clause box | The blockquote from that section, verbatim. **Bold** words in the markdown = **yellow highlight** |
| Body | The analysis paragraph(s) **verbatim** — do not shorten, do not turn into bullets, do not add “Diagram:” / “layout” / “prompt” language |
| Table | The markdown table, full width, readable type |
| Footer | The Chicago citation from that section (or the file-end citation if the section has none) |
| Title block | Bottom-right: `63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/40` (continuous numbering across all three parts) |

**Do not** invent numbers, reclassify as Class 2, reopen Hybrid A/C, or change the 6.0 m grid. One markdown `##` section = one sheet, in file order.

---

## Single prompt — one folio, all 40 sheets (copy everything below)

```
Build ONE A3 landscape PDF folio for RMIT ARCH3372 AT2 at 63–67 Nicholson St, Footscray — all three reports in a single 40-sheet project.

Connect GitHub repo https://github.com/feangkan/AAT_Tools on branch cursor/at2-week5-f836.

These are TEXT slides for tutor presentation — NOT AT1.4’s left-diagram / right-text layout. Copy all clause quotes, analysis, and tables verbatim from the markdown sources. Do not rewrite, shorten, or add “Diagram:”, “layout”, or AI-prompt language.

GLOBAL LAYOUT (every sheet):
A3 landscape 420 × 297 mm. Navy #1f4b66, white ground, black hairline border inset ~8 mm.
- Header: ARCH3372 · AT2.x · sheet title from the markdown ## N. … heading
- Clause box: the blockquote, verbatim. Yellow-highlight every **bold** phrase from the markdown.
- Body: the analysis paragraph(s) verbatim.
- Table: the section’s markdown table, full width, readable type.
- Footer: Chicago citation from that section (or the file-end citation if the section has none).
- Title block bottom-right: 63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/40

GLOBAL LOCKS:
Class 3 lodging + Class 6 retail. Hybrid B. 6.0 m grid. Do not reclassify to Class 2. Do not reopen Hybrid A/C. Do not invent numbers. One markdown ## section = one sheet, in file order.

SHEET ORDER (40 sheets total — continuous numbering 1/40 through 40/40):

PART A — AT2.1 NCC Report (sheets 1–12)
Source: docs/AT2.1-week5-NCC-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.1-week5-NCC-report.md
## 1 through ## 12 → sheets 1/40 through 12/40. Header prefix: ARCH3372 · AT2.1 NCC Report ·
Locks: Travel distances 6 m (SOU door to choice) / 20 m (corridor), not 40 m. Wet areas F2D2 + Spec 26, not Housing Provisions Part 10.2. Sprinklers E1D6, rise ≥ 4, effective height ≤ 25 m.

PART B — AT2.2 LHD + BADS Report (sheets 13–28)
Source: docs/AT2.2-lhd-bads-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.2-lhd-bads-report.md
## 1 through ## 16 → sheets 13/40 through 28/40. Header prefix: ARCH3372 · AT2.2 LHD & BADS ·
Locks: G7 is an amenity overlay, not a reclassification to Class 2. Keep honest conflicts on the page: D18 50% vs brief 1:20 DDA; D21 5 m³ vs 15–25 m² studio; D26 apartment sizes vs locked studio; D29 40% cross-vent vs double-loaded plate.

PART C — AT2.3 Environmental Design / Energy (sheets 29–40)
Source: docs/AT2.3-environmental-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.3-environmental-report.md
## 1 through ## 12 → sheets 29/40 through 40/40. Header prefix: ARCH3372 · AT2.3 Environmental Design ·
Locks: NCC climate zone 6. H6 does not apply (Class 1/10). J1P2 / J1P3 / J3 are Class 2 SOU headings. Class 3 pathway is J1P1 + J4 + J6. Class 3 CZ6 wall-glazing U1.1 / solar admittance 0.07, not Class 2 elemental U2.0 / 0.14.

Optional part-divider sheets: a simple navy band title page before sheet 1 (AT2.1), sheet 13 (AT2.2), and sheet 29 (AT2.3) — only if space allows; do not skip content sheets.

Export ONE 40-page A3 landscape PDF named AT2-Footscray-Complete.pdf

No photos required. Optional simple schematic only on sheet 10 (AT2.1 travel on 6.0 m floor) and sheet 25 (AT2.2 typical bay) — still text-led.
```

---

## How to run it

1. Open https://claude.ai/design
2. New project → import GitHub `feangkan/AAT_Tools` → branch `cursor/at2-week5-f836`
3. Paste the single prompt above (everything inside the code fence)
4. Export one PDF: `AT2-Footscray-Complete.pdf` (40 pages)

If GitHub import fails, paste all three `docs/AT2.x-….md` files into the chat as well as the prompt.

No photos are required for AT2. Do not invent precedent photography. Optional: a simple schematic only on AT2.1 sheet 10 (travel on the 6.0 m floor) and AT2.2 sheet 13 (typical bay) — still keep those sheets text-led.

---

*Production tool for Claude Design · ARCH3372 · AT2 · not for the tutor folio*
