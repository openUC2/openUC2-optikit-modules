#!/usr/bin/env python3
"""
generate_from_template.py — Generate a UC2 module from a category template.

This is the core automation script for Scenario 2 (generic parts).
Given a category (e.g., "lens") and a set of parameters, it generates
a complete module folder with all required files.

Usage:
    python scripts/generate_from_template.py \\
        --category lens \\
        --id lens-pcx-f100 \\
        --params '{"focalLength_mm": 100, "diameter_mm": 25.4, ...}'

    python scripts/generate_from_template.py \\
        --category lens \\
        --from-csv vendor-catalogs/thorlabs/planoconvex_lenses.csv
"""

import argparse
import json
import uuid
import shutil
import math
from datetime import date
from pathlib import Path
from string import Template

import yaml


REPO_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
MODULES_DIR = REPO_ROOT / "modules"


def generate_uuid():
    """Generate a new UUID v4."""
    return str(uuid.uuid4())


def load_template(category: str) -> dict:
    """Load the template definition for a category."""
    template_dir = TEMPLATES_DIR / category
    template_file = template_dir / "template.yaml"
    if not template_file.exists():
        raise FileNotFoundError(f"No template found for category: {category}")
    with open(template_file) as f:
        return yaml.safe_load(f)


def compute_derived_params(category: str, params: dict) -> dict:
    """Compute derived parameters from the given inputs."""
    derived = {}

    if category == "lens":
        r1 = params.get("curvature_r1_mm", float("inf"))
        r2 = params.get("curvature_r2_mm", float("inf"))
        ct = params.get("center_thickness_mm", 5.0)
        d = params.get("diameter_mm", 25.4)

        # Edge thickness for plano-convex (plano side is r1=inf)
        if r2 != float("inf") and r2 != 0:
            sag = abs(r2) - math.sqrt(r2**2 - (d/2)**2)
            derived["edge_thickness_mm"] = round(ct - sag, 2)
        else:
            derived["edge_thickness_mm"] = ct

        # Clear aperture (90% of diameter)
        derived["clear_aperture_mm"] = round(d * 0.9, 2)

    return derived


def generate_optiland_json(category: str, params: dict, mod_uuid: str, opt_uuid: str) -> dict:
    """Generate the Optiland JSON for the given parameters."""
    if category == "lens":
        r_convex = params.get("curvature_r2_mm", -25.8)
        ct = params.get("center_thickness_mm", 5.3)
        material = params.get("material", "N-BK7")
        diameter = params.get("diameter_mm", 25.4)
        f = params.get("focalLength_mm", 50.0)

        return {
            "_metadata": {
                "generator": "openuc2-optikit",
                "generator_version": "1.0.0",
                "optiland_version": ">=0.5.0",
                "uuid": opt_uuid,
                "module_uuid": mod_uuid,
                "description": f"Plano-convex lens, f={f}mm, Ø{diameter}mm, {material}",
                "repo": "https://github.com/openuc2/openuc2-optiland-models",
                "created": str(date.today()),
                "author": "openUC2 Team (auto-generated)",
            },
            "surfaces": [
                {
                    "index": 0,
                    "comment": "Object surface",
                    "type": "standard",
                    "radius": "Infinity",
                    "thickness": "Infinity",
                    "material": "air",
                    "is_stop": False,
                    "semi_aperture": diameter / 2,
                },
                {
                    "index": 1,
                    "comment": "Convex surface",
                    "type": "standard",
                    "radius": abs(r_convex),
                    "thickness": ct,
                    "material": {
                        "name": material,
                        "catalog": "schott",
                    },
                    "is_stop": True,
                    "semi_aperture": diameter / 2,
                },
                {
                    "index": 2,
                    "comment": "Plano surface",
                    "type": "standard",
                    "radius": "Infinity",
                    "thickness": f - ct,  # Approximate BFL
                    "material": "air",
                    "is_stop": False,
                    "semi_aperture": diameter / 2,
                },
                {
                    "index": 3,
                    "comment": "Image surface",
                    "type": "standard",
                    "radius": "Infinity",
                    "thickness": None,
                    "material": "air",
                    "is_stop": False,
                    "semi_aperture": 0.0,
                },
            ],
            "aperture": {"type": "EPD", "value": diameter},
            "fields": {"type": "angle", "values": [{"y": 0.0, "x": 0.0, "weight": 1.0}]},
            "wavelengths": [
                {"value_um": 0.4861, "weight": 1.0, "is_primary": False, "label": "F-line"},
                {"value_um": 0.5876, "weight": 1.0, "is_primary": True, "label": "d-line"},
                {"value_um": 0.6563, "weight": 1.0, "is_primary": False, "label": "C-line"},
            ],
        }

    raise NotImplementedError(f"Optiland generation not yet implemented for category: {category}")


def generate_module(category: str, module_id: str, params: dict, output_dir: Path = None):
    """Generate a complete module folder from a template and parameters."""
    mod_uuid = generate_uuid()
    opt_uuid = f"opt-{mod_uuid[:8]}-{category}-{module_id}"
    cad_uuid = f"cad-{mod_uuid[:8]}-{category}-{module_id}"

    if output_dir is None:
        output_dir = MODULES_DIR / module_id

    output_dir.mkdir(parents=True, exist_ok=True)

    # Compute derived params
    derived = compute_derived_params(category, params)
    all_params = {**params, **derived}

    # Generate module.yaml
    module_data = {
        "id": module_id,
        "uuid": mod_uuid,
        "name": params.get("name", f"{category.title()} ({module_id})"),
        "version": "1.0.0",
        "category": category,
        "scenario": 2,
        "group": params.get("group", f"{category}s"),
        "grid_size": [1, 1],
        "color": params.get("color", "#7CC142"),
        "metadata": {
            "author": "openUC2 Team (auto-generated)",
            "date": str(date.today()),
            "vendor": params.get("vendor", ""),
            "sku": params.get("sku", ""),
            "etag": "v4-auto",
            "license": "CERN-OHL-S-2.0",
        },
        "parameters": {
            "static": {k: v for k, v in all_params.items()
                       if k not in ("name", "group", "color", "vendor", "sku")},
            "variable": {
                "dz_mm": {
                    "default": 0.0, "min": -2.0, "max": 2.0,
                    "step": 0.1, "unit": "mm",
                }
            },
        },
        "ports": [
            {"id": "port-optical-in", "face": "+X", "type": "optical", "beam_height_mm": 25.0},
            {"id": "port-optical-out", "face": "-X", "type": "optical", "beam_height_mm": 25.0},
        ],
        "optics": {
            "optiland_file": "optics/optiland.json",
            "optiland_ref": {
                "repo": "https://github.com/openuc2/openuc2-optiland-models",
                "uuid": opt_uuid,
                "commit": None,
            },
        },
        "cad": {
            "inventor_assembly": None,
            "inventor_ref": {
                "repo": "https://github.com/openuc2/openuc2-cad-modules",
                "uuid": cad_uuid,
            },
            "exports": {
                "step": "cad/exports/model.step",
                "stl": "cad/exports/model.stl",
                "glb": "cad/exports/model.glb",
            },
            "bom": "cad/bom.yaml",
        },
        "electronics": {"has_electronics": False},
        "firmware": {"has_firmware": False},
        "software": {"imswitch": {"has_imswitch": False}},
        "configurator": {
            "icon": "configurator/icon.svg",
            "description": f"{category.title()} module (auto-generated)",
            "price_eur": params.get("price_eur", 0),
        },
        "production": {
            "printing": "production/printing.yaml",
            "supply_chain": "production/supply_chain.yaml",
        },
    }

    # Write module.yaml
    with open(output_dir / "module.yaml", "w") as f:
        yaml.dump(module_data, f, default_flow_style=False, sort_keys=False)

    # Generate and write Optiland JSON
    optics_dir = output_dir / "optics"
    optics_dir.mkdir(exist_ok=True)
    optiland_data = generate_optiland_json(category, params, mod_uuid, opt_uuid)
    with open(optics_dir / "optiland.json", "w") as f:
        json.dump(optiland_data, f, indent=2)

    # Create placeholder directories
    for subdir in ["cad/exports", "cad/drawings", "configurator",
                   "production", "docs", "software/imswitch", "software/examples",
                   "electronics", "firmware", "marketing/photos", "marketing/slides"]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)

    # Write README
    with open(output_dir / "README.md", "w") as f:
        f.write(f"# {module_data['name']}\n\n")
        f.write(f"**Module ID:** `{module_id}` | **UUID:** `{mod_uuid}`\n\n")
        f.write(f"Auto-generated from `templates/{category}/` on {date.today()}.\n\n")
        f.write(f"See `module.yaml` for full specification.\n")

    print(f"Generated module: {output_dir}")
    print(f"  UUID: {mod_uuid}")
    print(f"  Optiland ref: {opt_uuid}")
    print(f"  CAD ref: {cad_uuid}")

    return module_data


def main():
    parser = argparse.ArgumentParser(description="Generate UC2 module from template")
    parser.add_argument("--category", required=True, help="Module category (lens, mirror, ...)")
    parser.add_argument("--id", required=True, help="Module ID (e.g., lens-pcx-f100)")
    parser.add_argument("--params", type=str, help="JSON string of parameters")
    parser.add_argument("--from-csv", type=str, help="CSV file for batch generation")
    args = parser.parse_args()

    if args.params:
        params = json.loads(args.params)
        generate_module(args.category, args.id, params)
    elif args.from_csv:
        import csv
        with open(args.from_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric strings to numbers
                params = {}
                for k, v in row.items():
                    try:
                        params[k] = float(v)
                    except (ValueError, TypeError):
                        params[k] = v
                mid = row.get("id", f"{args.category}-{row.get('sku', 'unknown')}")
                generate_module(args.category, mid, params)
    else:
        print("ERROR: Provide either --params or --from-csv")
        sys.exit(1)


if __name__ == "__main__":
    main()
