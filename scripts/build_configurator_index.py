#!/usr/bin/env python3
"""
build_configurator_index.py — Build the modules.json index for the OptiKit web configurator.

Reads all module.yaml files and produces a single JSON file that the
web app consumes, matching the format of the existing modules_updated.csv.

Usage:
    python scripts/build_configurator_index.py
    python scripts/build_configurator_index.py --output configurator/modules.json
"""

import argparse
import json
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
MODULES_DIR = REPO_ROOT / "modules"
DEFAULT_OUTPUT = REPO_ROOT / "configurator" / "modules.json"


def build_index(modules_dir: Path) -> list[dict]:
    """Scan all modules and build the configurator index."""
    index = []

    for module_dir in sorted(modules_dir.iterdir()):
        if not module_dir.is_dir():
            continue

        module_yaml = module_dir / "module.yaml"
        if not module_yaml.exists():
            print(f"  SKIP {module_dir.name} (no module.yaml)")
            continue

        with open(module_yaml) as f:
            data = yaml.safe_load(f)

        if data is None:
            print(f"  SKIP {module_dir.name} (empty module.yaml)")
            continue

        # Build configurator entry (matches existing CSV schema)
        cfg = data.get("configurator", {})
        params = data.get("parameters", {}).get("static", {})
        grid = data.get("grid_size", [1, 1])
        sw = data.get("software", {}).get("imswitch", {})

        entry = {
            "id": data.get("id"),
            "uuid": data.get("uuid"),
            "name": data.get("name"),
            "group": data.get("group"),
            "color": data.get("color"),
            "width": grid[0],
            "height": grid[1],
            "thumbnail": cfg.get("icon", ""),
            "cadUrl": data.get("cad", {}).get("exports", {}).get("glb", ""),
            "description": cfg.get("description", ""),
            "defaultParams": json.dumps(params),
            "autodeskInventor": cfg.get("autodeskInventor", ""),
            "price": cfg.get("price_eur", 0),
            "notification": cfg.get("notification", ""),
            "ImSwitch": json.dumps(sw.get("config_snippet", {}))
                        if sw.get("has_imswitch") else "",
            # New fields
            "category": data.get("category"),
            "scenario": data.get("scenario"),
            "vendor": data.get("metadata", {}).get("vendor", ""),
            "sku": data.get("metadata", {}).get("sku", ""),
            "optiland_uuid": data.get("optics", {}).get("optiland_ref", {}).get("uuid", ""),
            "cad_uuid": data.get("cad", {}).get("inventor_ref", {}).get("uuid", ""),
        }

        index.append(entry)
        print(f"  ADD  {data.get('id')}")

    return index


def main():
    parser = argparse.ArgumentParser(description="Build configurator index")
    parser.add_argument("--output", type=str, default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Scanning modules in: {MODULES_DIR}")
    index = build_index(MODULES_DIR)

    with open(output_path, "w") as f:
        json.dump(index, f, indent=2)

    print(f"\nWrote {len(index)} modules to: {output_path}")


if __name__ == "__main__":
    main()
