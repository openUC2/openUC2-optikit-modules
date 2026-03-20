#!/usr/bin/env python3
"""Generate GLB preview from STL if missing. Requires trimesh."""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--if-missing", action="store_true")
    args = parser.parse_args()
    
    modules_dir = Path(__file__).parent.parent / "modules"
    for module_dir in sorted(modules_dir.iterdir()):
        if not module_dir.is_dir():
            continue
        glb = module_dir / "cad" / "exports" / "model.glb"
        stl = module_dir / "cad" / "exports" / "model.stl"
        if args.if_missing and glb.exists():
            continue
        if stl.exists() and not glb.exists():
            try:
                import trimesh
                mesh = trimesh.load(str(stl))
                mesh.export(str(glb), file_type="glb")
                print(f"Generated: {glb}")
            except Exception as e:
                print(f"Failed for {module_dir.name}: {e}")

if __name__ == "__main__":
    main()
