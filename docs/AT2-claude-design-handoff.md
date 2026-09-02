# AT2 → Claude Design

This file is a **production brief for Claude Design**, not the student folio. Tutors should not be shown this file.

**Week 6 update:** AT2.2 and AT2.3 are trimmed to match what's actually in your research pack — required course headings kept, unpulled extension slides removed — and corrected against the real Week 6 Revit model (3.6 × 7.2 m bay, not the earlier 6.0 m assumption). Every required slide that stays now also says whether the real drawing set actually shows what the clause needs, and what to add if it doesn't. Three new short reports are added — First Nations sourcing, facade panel strategy (now with a built precedent), and mass timber fire resistance. **AT2.1 has not been touched** (out of scope for this pass) and still reads against the older 6.0 m assumption — flag that to your tutor separately if it needs the same correction pass.

**Student-facing copy (source of truth — paste/layout from these, do not rewrite):**

| Folio | File | Sheets |
|---|---|---|
| AT2.1 NCC | [`docs/AT2.1-week5-NCC-report.md`](./AT2.1-week5-NCC-report.md) | 12 |
| AT2.2 LHD + BADS | [`docs/AT2.2-lhd-bads-report.md`](./AT2.2-lhd-bads-report.md) | 11 |
| AT2.3 Energy | [`docs/AT2.3-environmental-report.md`](./AT2.3-environmental-report.md) | 7 |
| First Nations sourcing | [`docs/AT2-first-nations-sourcing.md`](./AT2-first-nations-sourcing.md) | 2 |
| Facade strategy (TMT panel + precedent) | [`docs/AT2-facade-panel-strategy.md`](./AT2-facade-panel-strategy.md) | 3 |
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

Start at https://claude.ai/design · connect this GitHub repo on that branch · paste **the single prompt below** (one project, one 37-sheet PDF).

---

## Layout (all sheets)

These are **text slides**, not the AT1.4 half-diagram / half-text layout.

A3 landscape **420 × 297 mm**. Navy `#1f4b66`, white ground, black hairline border inset ~8 mm.

| Zone | What goes there |
|---|---|
| Header | `ARCH3372 · AT2.x · 63–67 Nicholson St, Footscray` · sheet title from the markdown `## N. …` heading |
| Clause box | The blockquote from that section, verbatim. **Bold** words in the markdown = **yellow highlight** |
| Body | The analysis paragraph(s) **verbatim** — do not shorten, do not turn into bullets, do not add “Diagram:” / “layout” / “prompt” language. Where a paragraph begins **"On the real drawing:"**, keep it as its own short paragraph, in a slightly smaller or boxed treatment if space allows — it is a distinct "status check" note, not part of the main analysis |
| Table | The markdown table, full width, readable type |
| Footer | The Chicago citation from that section (or the file-end citation if the section has none) |
| Title block | Bottom-right: `63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/37` (continuous numbering across all six parts) |

**Do not** invent numbers, reclassify as Class 2, reopen Hybrid A/C, or change the **3.6 × 7.2 m bay** (the Week 6-corrected grid — do not revert to a 6.0 m square). Where a table or "On the real drawing" note shows something genuinely **not yet resolved** (D27 depth, D20 balcony depth, a missing services sheet, an undimensioned detail) — keep that wording. Do not quietly round it to a pass or invent a drawing that doesn't exist yet. One markdown `##` section = one sheet, in file order.

---

## Single prompt — one folio, all 37 sheets (copy everything below)

```
Build ONE A3 landscape PDF folio for RMIT ARCH3372 AT2 at 63–67 Nicholson St, Footscray — six reports in a single 37-sheet project.

Connect GitHub repo https://github.com/feangkan/AAT_Tools on branch cursor/at2-week5-f836.

These are TEXT slides for tutor presentation — NOT AT1.4's left-diagram / right-text layout. Copy all clause quotes, analysis, and tables verbatim from the markdown sources. Do not rewrite, shorten, or add "Diagram:", "layout", or AI-prompt language.

GLOBAL LAYOUT (every sheet):
A3 landscape 420 × 297 mm. Navy #1f4b66, white ground, black hairline border inset ~8 mm.
- Header: ARCH3372 · AT2.x · sheet title from the markdown ## N. … heading
- Clause box: the blockquote, verbatim. Yellow-highlight every **bold** phrase from the markdown.
- Body: the analysis paragraph(s) verbatim. A paragraph starting "On the real drawing:" is a distinct status-check note (what the real Revit model shows vs. what's still missing) — keep it as its own short paragraph, do not merge it into the main analysis or delete it.
- Table: the section's markdown table, full width, readable type. Where a cell says something has NOT passed or is unresolved (e.g. "exceeds the limit", "short", "open risk", "Not yet placed"), keep that wording — do not soften it to a pass.
- Footer: Chicago citation from that section (or the file-end citation if the section has none).
- Title block bottom-right: 63–67 Nicholson St, Footscray · ACZ1 · Wurundjeri Country · Sheet x/37

GLOBAL LOCKS:
Class 3 lodging + Class 6 retail. Hybrid B. Structural bay is 3.6 m × 7.2 m (Week 6 Revit model, sheet A400) — do NOT use a 6.0 m square grid on sheets from AT2.2, AT2.3, First Nations, Facade, or Fire (AT2.1 alone still uses the older 6.0 m figure and has not been corrected — copy it as-is, do not silently fix it). Do not reclassify to Class 2. Do not reopen Hybrid A/C. Do not invent numbers. One markdown ## section = one sheet, in file order.

SHEET ORDER (37 sheets total — continuous numbering 1/37 through 37/37):

PART A — AT2.1 NCC Report (sheets 1–12)
Source: docs/AT2.1-week5-NCC-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.1-week5-NCC-report.md
## 1 through ## 12 → sheets 1/37 through 12/37. Header prefix: ARCH3372 · AT2.1 NCC Report ·
Locks: Travel distances 6 m (SOU door to choice) / 20 m (corridor), not 40 m. Wet areas F2D2 + Spec 26, not Housing Provisions Part 10.2. Sprinklers E1D6, rise ≥ 4, effective height ≤ 25 m. Note: this part still reads against the uncorrected 6.0 m grid — copy verbatim, do not fix.

PART B — AT2.2 LHD + BADS Report (sheets 13–23)
Source: docs/AT2.2-lhd-bads-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.2-lhd-bads-report.md
## 1 through ## 11 → sheets 13/37 through 23/37. Header prefix: ARCH3372 · AT2.2 LHD & BADS ·
Locks: real bay 3.6 × 7.2 m (Week 6 model). G7 is an amenity overlay, not a reclassification to Class 2. Keep honest conflicts on the page: D18 50% vs brief 1:20 DDA; D21 5 m³ vs 15–25 m² studio; D26 apartment sizes vs locked studio; D29 40% cross-vent vs double-loaded plate; D27 depth 7.2 m EXCEEDS the 6.75 m limit (sheet 19/37, ## 7); D20 balcony 6.48 m² SHORT of 8 m² at 1.8 m depth (sheet 16/37, ## 4). Every sheet in this part carries an "On the real drawing" status note — keep it verbatim, including any "not yet dimensioned" / "not yet tagged" wording.

PART C — AT2.3 Environmental Design / Energy (sheets 24–30)
Source: docs/AT2.3-environmental-report.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2.3-environmental-report.md
## 1 through ## 7 → sheets 24/37 through 30/37. Header prefix: ARCH3372 · AT2.3 Environmental Design ·
Locks: NCC climate zone 6. Real bay 3.6 × 7.2 m. H6 does not apply (Class 1/10). J1P2 / J1P3 / J3 are Class 2 SOU headings. Class 3 pathway is J1P1 + J4 + J6. Class 3 CZ6 wall-glazing U1.1 / solar admittance 0.07, not Class 2 elemental U2.0 / 0.14. Keep every "On the real drawing" note verbatim, including the ones stating no mechanical/services sheet exists yet — do not invent one.

PART D — First Nations Materials, Sourcing & Country (sheets 31–32)
Source: docs/AT2-first-nations-sourcing.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-first-nations-sourcing.md
## 1 through ## 2 → sheets 31/37 through 32/37. Header prefix: ARCH3372 · AT2 First Nations Sourcing ·
Locks: named real products (NeXTimber NX5-150/GL13, ASH MASSLAM SL33) with real Victorian mill locations. Keep the honest 0% Indigenous-owned-supply figure on the page — do not round it up or omit it. Include the sourcing table and the precedent table verbatim.

PART E — Facade Strategy: Modular TMT Panel (sheets 33–35)
Source: docs/AT2-facade-panel-strategy.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-facade-panel-strategy.md
## 1 through ## 3 → sheets 33/37 through 35/37. Header prefix: ARCH3372 · AT2 Facade Strategy ·
Locks: include the 5-row panel comparison table (TMT, HPL, fiber cement, terracotta, GFRC) in full on sheet 33/37. Include the build-up list and detail table on sheet 34/37. Sheet 35/37 is the Lumber 4 (Oslotre, Kristiansand) precedent — include the comparison table AND the "honest gap" paragraph noting Lumber 4 is fire-treated painted pine, not the same finish as the chosen TMT panel; do not blur the two into one material.

PART F — Mass Timber Fire Resistance (sheets 36–37)
Source: docs/AT2-fire-resistance.md
https://github.com/feangkan/AAT_Tools/blob/cursor/at2-week5-f836/docs/AT2-fire-resistance.md
## 1 through ## 2 → sheets 36/37 through 37/37. Header prefix: ARCH3372 · AT2 Fire Resistance ·
Locks: include the char-depth table with real member sizes (265×260 column, 135×630 beam) verbatim, including the flagged narrow-beam-width finding. Include the facade cavity-fire-interface table on sheet 37/37.

Optional part-divider sheets: a simple navy band title page before sheet 1 (AT2.1), sheet 13 (AT2.2), sheet 24 (AT2.3), sheet 31 (First Nations), sheet 33 (Facade), and sheet 36 (Fire) — only if space allows; do not skip content sheets.

Export ONE 37-page A3 landscape PDF named AT2-Footscray-Complete.pdf

No photos required, except sheet 35/37 (Lumber 4 precedent) may include one credited image of the building if the source page permits reuse — otherwise a schematic redraw. Optional simple schematic only on sheet 10 (AT2.1 travel distance diagram) and sheet 16 (AT2.2, D20 balcony) — still text-led.
```

---

## How to run it

1. Open https://claude.ai/design
2. New project → import GitHub `feangkan/AAT_Tools` → branch `cursor/at2-week5-f836`
3. Paste the single prompt above (everything inside the code fence)
4. Export one PDF: `AT2-Footscray-Complete.pdf` (37 pages)

If GitHub import fails, paste all six `docs/AT2*.md` files into the chat as well as the prompt.

**If you only want to revise your existing deck** rather than rebuild all 37 sheets: your existing pack already has (per the research file) AT2.1's content, the LHD Parts 3–6 slides (now AT2.2 sheets 22–23), and AT2.3's J3/J4/J6/J5 slides (now sheets 27–30). What's actually new to add: the required-but-unbuilt Clause 58 slides (AT2.2 sheets 13–21: G7, D18–D21, D26–D29) and H6/J1P2/J1P3 (AT2.3 sheets 24–26), plus Parts D, E, F (sheets 31–37) in full. Paste those as an "insert these sheets, renumber the rest to match" instruction rather than rebuilding from scratch.

---

*Production tool for Claude Design · ARCH3372 · AT2 · not for the tutor folio*
