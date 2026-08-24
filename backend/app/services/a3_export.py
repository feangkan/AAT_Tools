"""A3 landscape PDF export (420 × 297 mm)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit


PAGE = landscape(A3)  # 420mm x 297mm in points


def render_a3_pdf(
    path: Path,
    *,
    title: str,
    subtitle: str = "",
    sheets: list[dict[str, Any]],
    members: list[str] | None = None,
) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=PAGE)
    members = members or []
    total = max(1, len(sheets))

    for i, sheet in enumerate(sheets):
        _draw_sheet(
            c,
            folio_title=title,
            subtitle=subtitle or sheet.get("subtitle", ""),
            sheet_title=sheet.get("title", f"Sheet {i+1}"),
            body=sheet.get("body", ""),
            bullets=sheet.get("bullets", []),
            members=members,
            sheet_no=i + 1,
            sheet_total=total,
            meta=sheet.get("meta", {}),
        )
        c.showPage()
    c.save()
    return path


def _draw_sheet(
    c: canvas.Canvas,
    *,
    folio_title: str,
    subtitle: str,
    sheet_title: str,
    body: str,
    bullets: list[str],
    members: list[str],
    sheet_no: int,
    sheet_total: int,
    meta: dict[str, Any],
) -> None:
    w, h = PAGE
    margin = 12 * mm
    ink = HexColor("#111111")
    accent = HexColor("#1f4b66")
    rule = HexColor("#c5c5c5")

    # Outer frame
    c.setStrokeColor(ink)
    c.setLineWidth(1.2)
    c.rect(margin, margin, w - 2 * margin, h - 2 * margin)

    # Title block (right bottom) — architectural style
    tb_w, tb_h = 110 * mm, 28 * mm
    tb_x = w - margin - tb_w
    tb_y = margin
    c.setStrokeColor(ink)
    c.rect(tb_x, tb_y, tb_w, tb_h)
    c.setFillColor(accent)
    c.rect(tb_x, tb_y + tb_h - 8 * mm, tb_w, 8 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(tb_x + 3 * mm, tb_y + tb_h - 5.5 * mm, "AAT STUDIO TOOLS  |  ARCH3372")

    c.setFillColor(ink)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(tb_x + 3 * mm, tb_y + 18 * mm, folio_title[:48])
    c.setFont("Helvetica", 7)
    c.drawString(tb_x + 3 * mm, tb_y + 13 * mm, sheet_title[:52])
    if members:
        c.drawString(tb_x + 3 * mm, tb_y + 8 * mm, " / ".join(members)[:60])
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(tb_x + tb_w - 3 * mm, tb_y + 4 * mm, f"{sheet_no} / {sheet_total}")

    # Header band
    c.setStrokeColor(rule)
    c.setLineWidth(0.6)
    header_y = h - margin - 18 * mm
    c.line(margin + 4 * mm, header_y, w - margin - 4 * mm, header_y)
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin + 6 * mm, h - margin - 10 * mm, sheet_title)
    c.setFillColor(HexColor("#555555"))
    c.setFont("Helvetica", 9)
    c.drawString(margin + 6 * mm, h - margin - 15 * mm, subtitle[:90])

    # Body
    text_x = margin + 8 * mm
    text_y = header_y - 10 * mm
    max_width = w - 2 * margin - 20 * mm
    c.setFillColor(ink)
    c.setFont("Helvetica", 10)
    if body:
        lines = simpleSplit(body, "Helvetica", 10, max_width)
        for line in lines[:28]:
            c.drawString(text_x, text_y, line)
            text_y -= 5 * mm

    if bullets:
        text_y -= 4 * mm
        c.setFont("Helvetica-Bold", 10)
        c.drawString(text_x, text_y, "Key points")
        text_y -= 6 * mm
        c.setFont("Helvetica", 10)
        for b in bullets[:16]:
            wrapped = simpleSplit(f"• {b}", "Helvetica", 10, max_width)
            for line in wrapped:
                c.drawString(text_x, text_y, line)
                text_y -= 5 * mm
            text_y -= 1 * mm

    # Meta footer strip
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor("#666666"))
    meta_str = "  |  ".join(f"{k}: {v}" for k, v in list(meta.items())[:4])
    c.drawString(margin + 4 * mm, margin + 3 * mm, meta_str[:120])
