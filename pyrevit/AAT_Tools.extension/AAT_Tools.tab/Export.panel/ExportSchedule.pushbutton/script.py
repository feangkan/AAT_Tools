"""Export room/area schedule-like CSV for Inspector feedback loop."""
# -*- coding: utf-8 -*-
__title__ = "Export\nSchedule CSV"
__doc__ = "Exports room names/areas to ~/Documents/aat_tools/revit_rooms.csv for the web Inspector."

import csv
import os
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

OUT_DIR = os.path.join(os.path.expanduser("~"), "Documents", "aat_tools")
OUT = os.path.join(OUT_DIR, "revit_rooms.csv")


def main():
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)
    rooms = (
        FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Rooms)
        .WhereElementIsNotElementType()
        .ToElements()
    )
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "number", "level", "area_sqm"])
        for r in rooms:
            try:
                name = r.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
                number = r.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
                area_ft2 = r.get_Parameter(BuiltInParameter.ROOM_AREA).AsDouble()
                area_m2 = area_ft2 * 0.092903
                level = r.Level.Name if r.Level else ""
                w.writerow([name, number, level, round(area_m2, 2)])
            except Exception:
                continue
    print("Wrote {}".format(OUT))


if __name__ == "__main__":
    main()
