# AT2 → Claude Design

This file is a **production brief for Claude Design**, not the student folio. Tutors should not be shown this file.

**Week 6 update:** AT2.2 and AT2.3 are corrected against the real Week 6 Revit model (3.6 × 7.2 m bay, not the earlier 6.0 m assumption), and three new short reports are added — First Nations sourcing, facade panel strategy, and mass timber fire resistance. **AT2.1 has not been touched** (out of scope for this pass) and still reads against the older 6.0 m assumption — flag that to your tutor separately if it needs the same correction pass.

**Student-facing copy (source of truth — paste/layout from these, do not rewrite):**

| Folio | File | Sheets |
|---|---|---|
| AT2.1 NCC | [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) | 12 |
| AT2.2 LHD + BADS | [`docs/AT2.2-lhd-bads-report.md`](./AT2.2-lhd-bads-report.md) | 16 |
| AT2.3 Energy | [`docs/AT2.3-environmental-report.md`](./AT2.3-environmental-report.md) | 12 |
| First Nations sourcing | [`docs/AT2-first-nations-sourcing.md`](./AT2-first-nations-sourcing.md) | 2 |
| Facade strategy (TMT panel) | [`docs/AT2-facade-panel-strategy.md`](./AT2-facade-panel-strategy.md) | 2 |
| Mass timber fire resistance | [`docs/AT2-fire-resistance.md`](./AT2-fire-resistance.md) | 2 |

**Repo / branch to connect in Claude Design**

- Repo: https://github.com/feangkan/AAT_Tools
- Branch: `cursor/at2-week5-f836`
- AT2.1: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.1-week5-NCC-report.md
- AT2.2: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.2-lhd-bads-report.md
- AT2.3: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.3-environmental-report.md
- First Nations: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-first-nations-sourcing.md
- Facade: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-facade-panel-strategy.md
- Fire: https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-fire-resistance.md

Start at https://claude.ai/design · connect this GitHub repo on that branch · paste **the single prompt below** (one project, one 46-sheet PDF).

---

## Layout (all sheets)

These are **text slides**, not the AT1.4 half-diagram / half-text layout.

A3 landscape **420 × 297 mm**. Navy `#1f4b66`, white ground, black hairline border inset ~8 mm.

| Zone | What goes there |
|---|---|
| Header | `ARCH3372 · AT2.x · 63–67 Nicholson St, Footscray` · sheet title from the markdown `## N. …` heading |
| Clause box | The blockquote from that section, verbatim. **Bold** words in the markdown = **yellow highlight** |
| Body | The analysis paragraph(s) **verbatim** — do not shorten, do not turn into bullets, do not add “Diagram:” / “layout” / “prompt” language |
| Table | The markdown table, full width, readable type |
| Footer | The Chicago citation from that section (or the file-end citation if the section has none) |
| Title block | Bottom-right: `63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/46` (continuous numbering across all six parts) |

**Do not** invent numbers, reclassify as Class 2, reopen Hybrid A/C, or change the **3.6 × 7.2 m bay** (the Week 6-corrected grid — do not revert to a 6.0 m square). Where a table shows a clause that is genuinely **not yet resolved** (D27 depth, D20 balcony depth) — for example a cell reading "exceeds the limit" or "short" or "unresolved risk" — keep that wording on the slide. Do not quietly round it to a pass. One markdown `##` section = one sheet, in file order.

---

## Single prompt — one folio, all 46 sheets (copy everything below)

```
Build ONE A3 landscape PDF folio for RMIT ARCH3372 AT2 at 63–67 Nicholson St, Footscray — six reports in a single 46-sheet project.

Connect GitHub repo https://github.com/feangkan/AAT_Tools on branch cursor/at2-week5-f836.

These are TEXT slides for tutor presentation — NOT AT1.4's left-diagram / right-text layout. Copy all clause quotes, analysis, and tables verbatim from the markdown sources. Do not rewrite, shorten, or add "Diagram:", "layout", or AI-prompt language.

GLOBAL LAYOUT (every sheet):
A3 landscape 420 × 297 mm. Navy #1f4b66, white ground, black hairline border inset ~8 mm.
- Header: ARCH3372 · AT2.x · sheet title from the markdown ## N. … heading
- Clause box: the blockquote, verbatim. Yellow-highlight every **bold** phrase from the markdown.
- Body: the analysis paragraph(s) verbatim.
- Table: the section's markdown table, full width, readable type. Where a cell says something has NOT passed or is unresolved (e.g. "exceeds the limit", "short", "open risk"), keep that wording — do not soften it to a pass.
- Footer: Chicago citation from that section (or the file-end citation if the section has none).
- Title block bottom-right: 63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/46

GLOBAL LOCKS:
Class 3 lodging + Class 6 retail. Hybrid B. Structural bay is 3.6 m × 7.2 m (Week 6 Revit model, sheet A400) — do NOT use a 6.0 m square grid on sheets from AT2.2, AT2.3, First Nations, Facade, or Fire (AT2.1 alone still uses the older 6.0 m figure and has not been corrected — copy it as-is, do not silently fix it). Do not reclassify to Class 2. Do not reopen Hybrid A/C. Do not invent numbers. One markdown ## section = one sheet, in file order.

SHEET ORDER (46 sheets total — continuous numbering 1/46 through 46/46):

PART A — AT2.1 NCC Report (sheets 1–12)
Source: docs/AT2.1-week5-NCC-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.1-week5-NCC-report.md
## 1 through ## 12 → sheets 1/46 through 12/46. Header prefix: ARCH3372 · AT2.1 NCC Report ·
Locks: Travel distances 6 m (SOU door to choice) / 20 m (corridor), not 40 m. Wet areas F2D2 + Spec 26, not Housing Provisions Part 10.2. Sprinklers E1D6, rise ≥ 4, effective height ≤ 25 m. Note: this part still reads against the uncorrected 6.0 m grid — copy verbatim, do not fix.

PART B — AT2.2 LHD + BADS Report (sheets 13–28)
Source: docs/AT2.2-lhd-bads-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.2-lhd-bads-report.md
## 1 through ## 16 → sheets 13/46 through 28/46. Header prefix: ARCH3372 · AT2.2 LHD & BADS ·
Locks: real bay 3.6 × 7.2 m (Week 6 model). G7 is an amenity overlay, not a reclassification to Class 2. Keep honest conflicts on the page: D18 50% vs brief 1:20 DDA; D21 5 m³ vs 15–25 m² studio; D26 apartment sizes vs locked studio; D29 40% cross-vent vs double-loaded plate; D27 depth 7.2 m EXCEEDS the 6.75 m limit (sheet 19/46, ## 7); D20 balcony 6.48 m² SHORT of 8 m² at 1.8 m depth (sheet 16/46, ## 4, and sheet 25/46, ## 13). Keep these as open risks, not passes.

PART C — AT2.3 Environmental Design / Energy (sheets 29–40)
Source: docs/AT2.3-environmental-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.3-environmental-report.md
## 1 through ## 12 → sheets 29/46 through 40/46. Header prefix: ARCH3372 · AT2.3 Environmental Design ·
Locks: NCC climate zone 6. Real bay 3.6 × 7.2 m. H6 does not apply (Class 1/10). J1P2 / J1P3 / J3 are Class 2 SOU headings. Class 3 pathway is J1P1 + J4 + J6. Class 3 CZ6 wall-glazing U1.1 / solar admittance 0.07, not Class 2 elemental U2.0 / 0.14.

PART D — First Nations Materials, Sourcing & Country (sheets 41–42)
Source: docs/AT2-first-nations-sourcing.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-first-nations-sourcing.md
## 1 through ## 2 → sheets 41/46 through 42/46. Header prefix: ARCH3372 · AT2 First Nations Sourcing ·
Locks: named real products (NeXTimber NX5-150/GL13, ASH MASSLAM SL33) with real Victorian mill locations. Keep the honest 0% Indigenous-owned-supply figure on the page — do not round it up or omit it. Include the sourcing table and the precedent table verbatim.

PART E — Facade Strategy: Modular TMT Panel (sheets 43–44)
Source: docs/AT2-facade-panel-strategy.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-facade-panel-strategy.md
## 1 through ## 2 → sheets 43/46 through 44/46. Header prefix: ARCH3372 · AT2 Facade Strategy ·
Locks: include the 5-row panel comparison table (TMT, HPL, fiber cement, terracotta, GFRC) in full on sheet 43/46. Include the build-up list and detail table on sheet 44/46.

PART F — Mass Timber Fire Resistance (sheets 45–46)
Source: docs/AT2-fire-resistance.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-fire-resistance.md
## 1 through ## 2 → sheets 45/46 through 46/46. Header prefix: ARCH3372 · AT2 Fire Resistance ·
Locks: include the char-depth table with real member sizes (265×260 column, 135×630 beam) verbatim, including the flagged narrow-beam-width finding. Include the facade cavity-fire-interface table on sheet 46/46.

Optional part-divider sheets: a simple navy band title page before sheet 1 (AT2.1), sheet 13 (AT2.2), sheet 29 (AT2.3), sheet 41 (First Nations), sheet 43 (Facade), and sheet 45 (Fire) — only if space allows; do not skip content sheets.

Export ONE 46-page A3 landscape PDF named AT2-Footscray-Complete.pdf

No photos required. Optional simple schematic only on sheet 10 (AT2.1 travel distance diagram) and sheet 25 (AT2.2 typical bay, 3.6 × 7.2 m) — still text-led.
```

---

## How to run it

1. Open https://claude.ai/design
2. New project → import GitHub `feangkan/AAT_Tools` → branch `cursor/at2-week5-f836`
3. Paste the single prompt above (everything inside the code fence)
4. Export one PDF: `AT2-Footscray-Complete.pdf` (46 pages)

If GitHub import fails, paste all six `docs/AT2*.md` files into the chat as well as the prompt.

No photos are required for AT2. Do not invent precedent photography. Optional: a simple schematic only on AT2.1 sheet 10 (travel distance diagram) and AT2.2 sheet 25 (typical bay, 3.6 × 7.2 m) — still keep those sheets text-led.

**If you only want to revise the existing 40-sheet deck** rather than rebuild all 46: paste just the Part D/E/F blocks above (First Nations, Facade, Fire) as an "append 6 more sheets, continue numbering from 40/40 to 46/46" instruction, and separately re-paste Part B (AT2.2) alone as an "replace sheets 13–28 with this corrected version" instruction, since that is the part with real content changes (3.6 × 7.2 m bay, D27/D20 flags). Part A (AT2.1) and Part C (AT2.3, only wording touch-ups) do not need a forced re-render if your existing sheets already look right — check them against the current markdown first.

---

*Production tool for Claude Design · ARCH3372 · AT2 · not for the tutor folio*
