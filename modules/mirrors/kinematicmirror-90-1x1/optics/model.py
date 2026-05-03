"""
Optical model for UC2 module: kinematicmirror-90-1x1
Thorlabs POLARIS-K1 + BB1-E02 - Two-axis kinematic mount oriented for normal-incidence retro-reflection (mirror perpendicular to beam)

UUID: opt-c3d4e5f6-mirror-90deg
Module UUID: c3d4e5f6-a7b8-9012-cdef-345678901234
"""

import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants for this part
# ---------------------------------------------------------------------------
PART = {
    "vendor": "Thorlabs",
    "sku":    "POLARIS-K1 + BB1-E02",
    "uuid":   "opt-c3d4e5f6-mirror-90deg",
}

MIRROR_PARAMS = {
    "diameter_mm":         25.4,
    "thickness_mm":        6.0,
    "mirror_angle_deg":    90.0,
    "fold_angle_deg":      180.0,
    "reflectance_pct":     99.0,
    "wavelength_range_nm": [400, 750],
    "tilt_range_deg":      4.0,
}


def build_mirror():
    """Construct an Optiland Optic instance for this mirror."""
    from optiland import optic

    m = optic.Optic()
    m.add_surface(index=0, radius=np.inf, thickness=25.0)
    m.add_surface(
        index=1, radius=np.inf, thickness=0.0,
        material="mirror", is_stop=True,
        ry=np.deg2rad(MIRROR_PARAMS["mirror_angle_deg"]),
    )
    m.add_surface(index=2)
    m.set_aperture(aperture_type="EPD", value=MIRROR_PARAMS["diameter_mm"])
    m.set_field_type(field_type="angle")
    m.add_field(y=0.0)
    m.add_wavelength(value=0.488)
    m.add_wavelength(value=0.532, is_primary=True)
    m.add_wavelength(value=0.635)
    return m


def mirror_matrix():
    """Identity ray-transfer matrix for a flat mirror."""
    return np.eye(2)


def info() -> None:
    """Print a one-line headline with the headline specs."""
    print("=" * 60)
    print(f"  {PART['vendor']} {PART['sku']}")
    print("=" * 60)


def save_optiland_json(obj, filepath="optiland.json"):
    """Export to Optiland's native JSON format."""
    from optiland.fileio import save_optiland_file
    save_optiland_file(obj, filepath)
    print(f"Saved Optiland JSON to: {filepath}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Optical model for kinematicmirror-90-1x1")
    parser.add_argument("--save", type=str, default=None,
                        help="Export Optiland JSON to this filepath")
    args = parser.parse_args()
    info()
    try:
        builder = next(v for k, v in globals().items()
                       if k.startswith("build_") and callable(v))
        obj = builder()
        if args.save:
            save_optiland_json(obj, args.save)
        else:
            obj.info()
    except Exception as exc:
        print(f"  (optiland not installed or build failed: {exc})")
