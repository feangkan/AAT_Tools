"""Create A3 landscape sheets with title block placeholder."""
# -*- coding: utf-8 -*-
__title__ = "Make A3\nSheets"
__doc__ = "Creates A3 landscape sheets (420x297mm) for the AAT folio."

from Autodesk.Revit.DB import (
    Transaction,
    FilteredElementCollector,
    BuiltInCategory,
    XYZ,
    ViewSheet,
)

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


def main():
    # Find any title block family symbol
    tbs = FilteredElementCollector(doc).OfCategory(
        BuiltInCategory.OST_TitleBlocks
    ).WhereElementIsElementType().ToElements()
    if not tbs:
        print("Load an A3 landscape title block family first.")
        return
    tb = tbs[0]
    t = Transaction(doc, "AAT Make A3 Sheets")
    t.Start()
    try:
        for i, name in enumerate(
            ["AAT-Site", "AAT-Planning", "AAT-Massing", "AAT-Typical", "AAT-NCC"], 1
        ):
            sheet = ViewSheet.Create(doc, tb.Id)
            sheet.Name = name
            sheet.SheetNumber = "AAT-{:02d}".format(i)
        t.Commit()
    except Exception:
        t.RollBack()
        raise


if __name__ == "__main__":
    main()
