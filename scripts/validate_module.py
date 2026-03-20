#!/usr/bin/env python3
"""
validate_module.py — Validate UC2 module folders against the schema.

Usage:
    python scripts/validate_module.py                    # Validate all modules
    python scripts/validate_module.py --changed          # Only changed modules (CI)
    python scripts/validate_module.py --module lens-pos-1x1  # Specific module
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)


REPO_ROOT = Path(__file__).parent.parent
MODULES_DIR = REPO_ROOT / "modules"
SCHEMA_FILE = REPO_ROOT / "schemas" / "module.schema.json"


def load_yaml(path: Path) -> dict:
    """Load a YAML file, returning its contents as a dict."""
    with open(path) as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    with open(path) as f:
        return json.load(f)


def validate_schema(module_data: dict, schema: dict) -> list[str]:
    """Validate module.yaml against the JSON Schema."""
    errors = []
    validator = jsonschema.Draft202012Validator(schema)
    for error in validator.iter_errors(module_data):
        errors.append(f"  Schema: {error.json_path} — {error.message}")
    return errors


def validate_file_references(module_dir: Path, module_data: dict) -> list[str]:
    """Check that all referenced files actually exist."""
    errors = []
    files_to_check = []

    # Optics files
    optics = module_data.get("optics", {})
    if optics.get("optiland_file"):
        files_to_check.append(("optics.optiland_file", optics["optiland_file"]))
    if optics.get("model_file"):
        files_to_check.append(("optics.model_file", optics["model_file"]))
    if optics.get("coordinate_system"):
        files_to_check.append(("optics.coordinate_system", optics["coordinate_system"]))
    if optics.get("variable_parameters"):
        files_to_check.append(("optics.variable_parameters", optics["variable_parameters"]))

    # CAD exports
    cad = module_data.get("cad", {})
    exports = cad.get("exports", {})
    for fmt in ["step", "stl", "glb"]:
        if exports.get(fmt):
            files_to_check.append((f"cad.exports.{fmt}", exports[fmt]))
    if cad.get("bom"):
        files_to_check.append(("cad.bom", cad["bom"]))

    # Configurator assets
    cfg = module_data.get("configurator", {})
    if cfg.get("icon"):
        files_to_check.append(("configurator.icon", cfg["icon"]))

    # Check each file
    for label, rel_path in files_to_check:
        full_path = module_dir / rel_path
        if not full_path.exists():
            errors.append(f"  Missing file: {label} -> {rel_path}")

    return errors


def validate_optiland_json(module_dir: Path, module_data: dict) -> list[str]:
    """Basic sanity checks on the Optiland JSON."""
    errors = []
    optiland_path = module_data.get("optics", {}).get("optiland_file")
    if not optiland_path:
        return errors

    full_path = module_dir / optiland_path
    if not full_path.exists():
        return errors  # Already caught by file reference check

    try:
        data = load_json(full_path)
    except json.JSONDecodeError as e:
        errors.append(f"  Optiland JSON parse error: {e}")
        return errors

    surfaces = data.get("surfaces", [])
    if len(surfaces) < 3:
        errors.append(f"  Optiland JSON: Expected at least 3 surfaces, got {len(surfaces)}")

    if not data.get("wavelengths"):
        errors.append("  Optiland JSON: No wavelengths defined")

    if not data.get("aperture"):
        errors.append("  Optiland JSON: No aperture defined")

    return errors


def validate_csys_alignment(module_dir: Path) -> list[str]:
    """Check that optical and CAD coordinate systems reference each other."""
    errors = []
    opt_csys = module_dir / "optics" / "coordinate_system.yaml"
    cad_csys = module_dir / "cad" / "coordinate_system.yaml"

    if opt_csys.exists() and cad_csys.exists():
        opt_data = load_yaml(opt_csys)
        cad_data = load_yaml(cad_csys)

        opt_uuid = opt_data.get("module_uuid")
        cad_uuid = cad_data.get("module_uuid")

        if opt_uuid and cad_uuid and opt_uuid != cad_uuid:
            errors.append(
                f"  CSYS mismatch: optics module_uuid={opt_uuid} "
                f"!= cad module_uuid={cad_uuid}"
            )

    return errors


def validate_module(module_dir: Path, schema: dict) -> tuple[bool, list[str]]:
    """Run all validations on a single module."""
    errors = []
    module_yaml = module_dir / "module.yaml"

    if not module_yaml.exists():
        return False, [f"  No module.yaml found in {module_dir}"]

    try:
        data = load_yaml(module_yaml)
    except yaml.YAMLError as e:
        return False, [f"  YAML parse error: {e}"]

    if data is None:
        return False, ["  module.yaml is empty"]

    errors.extend(validate_schema(data, schema))
    errors.extend(validate_file_references(module_dir, data))
    errors.extend(validate_optiland_json(module_dir, data))
    errors.extend(validate_csys_alignment(module_dir))

    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser(description="Validate UC2 modules")
    parser.add_argument("--module", type=str, help="Validate a specific module by ID")
    parser.add_argument("--changed", action="store_true",
                        help="Only validate modules changed in this PR (requires git)")
    args = parser.parse_args()

    if not SCHEMA_FILE.exists():
        print(f"ERROR: Schema file not found: {SCHEMA_FILE}")
        sys.exit(1)

    schema = load_json(SCHEMA_FILE)

    # Determine which modules to validate
    if args.module:
        module_dirs = [MODULES_DIR / args.module]
    elif args.changed:
        import subprocess
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        changed_modules = set()
        for line in result.stdout.strip().split("\n"):
            if line.startswith("modules/"):
                parts = line.split("/")
                if len(parts) >= 2:
                    changed_modules.add(parts[1])
        module_dirs = [MODULES_DIR / m for m in sorted(changed_modules)]
    else:
        module_dirs = sorted(
            d for d in MODULES_DIR.iterdir() if d.is_dir()
        )

    if not module_dirs:
        print("No modules to validate.")
        sys.exit(0)

    # Run validation
    total = 0
    passed = 0
    failed = 0

    for module_dir in module_dirs:
        if not module_dir.exists():
            print(f"SKIP  {module_dir.name} (directory not found)")
            continue

        total += 1
        ok, errors = validate_module(module_dir, schema)

        if ok:
            passed += 1
            print(f"PASS  {module_dir.name}")
        else:
            failed += 1
            print(f"FAIL  {module_dir.name}")
            for err in errors:
                print(err)

    print(f"\n{'='*60}")
    print(f"Results: {passed}/{total} passed, {failed} failed")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
