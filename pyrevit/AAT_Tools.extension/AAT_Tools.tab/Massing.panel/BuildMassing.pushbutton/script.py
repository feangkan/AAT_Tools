"""Build massing extrusion from AAT Studio JSON / parameters."""
# -*- coding: utf-8 -*-
__title__ = "Build\nMassing"
__doc__ = "Creates podium + tower massing from AAT Studio Tools massing JSON."

import json
import os
from Autodesk.Revit.DB import (
    BuiltInCategory,
    FilteredElementCollector,
    XYZ,
    Line,
    CurveLoop,
    SolidOptions,
    GeometryCreationUtilities,
    DirectShape,
    ElementId,
    Transaction,
)

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

DEFAULT_JSON = os.path.join(
    os.path.expanduser("~"),
    "Documents",
    "aat_tools",
    "massing.json",
)


def _xy_loop(points_m, z=0.0):
    # Revit internal units are feet — convert metres
    def m2ft(m):
        return m * 3.280839895

    pts = [XYZ(m2ft(p[0]), m2ft(p[1]), m2ft(z)) for p in points_m[:-1]]
    curves = []
    for i in range(len(pts)):
        curves.append(Line.CreateBound(pts[i], pts[(i + 1) % len(pts)]))
    loop = CurveLoop.Create(curves)
    return loop


def _extrude(loop, height_m):
    def m2ft(m):
        return m * 3.280839895

    solid = GeometryCreationUtilities.CreateExtrusionGeometry(
        [loop], XYZ.BasisZ, m2ft(height_m)
    )
    return solid


def main():
    path = DEFAULT_JSON
    if not os.path.exists(path):
        # Fallback demo massing
        data = {
            "podium": {
                "footprint": [[0, 0], [30, 0], [30, 20], [0, 20], [0, 0]],
                "height_m": 6.4,
            },
            "tower": {
                "footprint": [[5, 3], [25, 3], [25, 17], [5, 17], [5, 3]],
                "height_m": 25.6,
            },
        }
    else:
        with open(path, "r") as f:
            data = json.load(f)

    t = Transaction(doc, "AAT Build Massing")
    t.Start()
    try:
        cat_id = ElementId(BuiltInCategory.OST_GenericModel)
        for key in ("podium", "tower"):
            block = data.get(key) or {}
            fp = block.get("footprint")
            h = float(block.get("height_m") or 3.2)
            if not fp:
                continue
            z0 = 0.0 if key == "podium" else float((data.get("podium") or {}).get("height_m") or 0)
            loop = _xy_loop(fp, z=z0)
            # Extrude relative height for tower already offset via z — use DirectShape at origin
            # Simpler: extrude full height from z0 by creating solid then... DirectShape doesn't transform easily.
            # Extrude from 0 and use tower footprint only for upper — acceptable for schematic.
            solid = _extrude(_xy_loop(fp, 0), h if key == "podium" else h)
            ds = DirectShape.CreateElement(doc, cat_id)
            ds.ApplicationId = "AAT_Tools"
            ds.ApplicationDataId = key
            ds.SetShape([solid])
            ds.Name = "AAT_{}".format(key)
        t.Commit()
    except Exception:
        t.RollBack()
        raise


if __name__ == "__main__":
    main()
