"""Generate typical floor room rectangles from AAT layout JSON as detail lines / filled regions proxy."""
# -*- coding: utf-8 -*-
__title__ = "Import\nFloor JSON"
__doc__ = "Reads typical/ground floor revit_json and draws model lines on the active view."

import json
import os
from Autodesk.Revit.DB import (
    XYZ,
    Line,
    Transaction,
    FilteredElementCollector,
    BuiltInCategory,
)

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
view = doc.ActiveView

DEFAULT_JSON = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "aat_tools",
    "typical_floor.json",
)


def m2ft(m):
    return m * 3.280839895


def main():
    path = DEFAULT_JSON
    if not os.path.exists(path):
        print("Place layout JSON at {}".format(path))
        return
    with open(path, "r") as f:
        data = json.load(f)
    rooms = data.get("rooms") or data.get("revit_json", {}).get("rooms") or []
    t = Transaction(doc, "AAT Import Floor JSON")
    t.Start()
    try:
        for r in rooms:
            x, y, w, d = float(r["x"]), float(r["y"]), float(r["w"]), float(r["d"])
            p0 = XYZ(m2ft(x), m2ft(y), 0)
            p1 = XYZ(m2ft(x + w), m2ft(y), 0)
            p2 = XYZ(m2ft(x + w), m2ft(y + d), 0)
            p3 = XYZ(m2ft(x), m2ft(y + d), 0)
            for a, b in ((p0, p1), (p1, p2), (p2, p3), (p3, p0)):
                doc.Create.NewDetailCurve(view, Line.CreateBound(a, b))
        t.Commit()
    except Exception:
        t.RollBack()
        raise


if __name__ == "__main__":
    main()
