#!/usr/bin/env python3
"""Check coordinate system alignment between optics and CAD."""
import argparse
from pathlib import Path
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--changed", action="store_true")
    args = parser.parse_args()
    
    modules_dir = Path(__file__).parent.parent / "modules"
    errors = 0
    for module_dir in sorted(modules_dir.iterdir()):
        if not module_dir.is_dir():
            continue
        opt = module_dir / "optics" / "coordinate_system.yaml"
        cad = module_dir / "cad" / "coordinate_system.yaml"
        if opt.exists() and cad.exists():
            with open(opt) as f:
                opt_data = yaml.safe_load(f)
            with open(cad) as f:
                cad_data = yaml.safe_load(f)
            if opt_data.get("module_uuid") != cad_data.get("module_uuid"):
                print(f"MISMATCH {module_dir.name}: UUID mismatch in CSYS files")
                errors += 1
            else:
                print(f"OK {module_dir.name}")
    return errors

if __name__ == "__main__":
    import sys
    sys.exit(main())
