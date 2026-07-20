"""Detail / facade / structure / precedents helpers."""

from __future__ import annotations

from typing import Any


def structural_options() -> dict[str, Any]:
    return {
        "options": [
            {
                "id": "mass_timber",
                "name": "Mass timber (CLT + glulam)",
                "pros": [
                    "Lower embodied carbon",
                    "Prefabrication / speed",
                    "Warm interior character for student housing",
                ],
                "cons": ["Acoustic build-ups", "Fire engineering", "Moisture control"],
                "grid_m": [6.0, 7.2],
                "references": [
                    "resources/klh-building-system-multi-story-residential-buildings.pdf",
                    "resources/5-MassTimberPedagogy-101-StructuralBasics.pdf",
                ],
                "country_note": "Explore First Nations timber suppliers and construction knowledge (PC36 / AT1.4).",
            },
            {
                "id": "concrete",
                "name": "Reinforced concrete frame / PT slabs",
                "pros": ["Acoustic mass", "Familiar local industry", "Long spans"],
                "cons": ["High embodied carbon", "Slower formwork"],
                "grid_m": [8.0, 8.4],
                "references": [],
            },
            {
                "id": "steel",
                "name": "Steel frame + composite slabs",
                "pros": ["Speed", "Long span retail podium", "Light structure"],
                "cons": ["Fire protection", "Thermal bridging", "Embodied carbon"],
                "grid_m": [7.5, 9.0],
                "references": [],
            },
        ],
        "recommendation": "Hybrid: concrete/steel podium for retail + mass-timber residential tower (KLH precedents).",
    }


def facade_templates() -> dict[str, Any]:
    return {
        "bay_types": [
            {
                "id": "studio_bay",
                "width_m": 3.6,
                "height_m": 3.2,
                "window_to_floor_pct": 12,
                "notes": "Meets ≥10% daylight WFR; operable sash for natural ventilation",
            },
            {
                "id": "corner_bay",
                "width_m": 4.2,
                "height_m": 3.2,
                "window_to_floor_pct": 18,
                "notes": "Cross-ventilation opportunity for Clause 58 breeze path",
            },
            {
                "id": "communal_bay",
                "width_m": 6.0,
                "height_m": 3.5,
                "window_to_floor_pct": 25,
                "notes": "Lounge / study transparency to street",
            },
        ],
        "wall_buildups": [
            {
                "id": "timber_batten_acoustic",
                "layers": [
                    "CLT or stud frame",
                    "Acoustic batts",
                    "Mounting tracks @ 600mm (timber) / 1200mm (alu)",
                    "Acoustic backing",
                    "Spotted Gum battens (AS5604 Class 1)",
                ],
                "source": "AT3.2 lighting/acoustics brief guidance",
            }
        ],
    }


def precedents_template() -> dict[str, Any]:
    return {
        "task": "AT1.3 Precedent Project Report",
        "required_buildings": 6,
        "a3_per_building": 2,
        "present_best": 3,
        "analysis_lenses": [
            "Structural systems",
            "Façade systems / detailing",
            "Environmental systems",
            "Services and core layouts",
            "Mechanical systems",
            "Finishes, fixtures, specified products",
        ],
        "slots": [
            {
                "id": i + 1,
                "name": "",
                "location": "",
                "storeys": None,
                "structure": "",
                "facade": "",
                "core": "",
                "notes": "",
                "selected_for_presentation": False,
            }
            for i in range(6)
        ],
    }
