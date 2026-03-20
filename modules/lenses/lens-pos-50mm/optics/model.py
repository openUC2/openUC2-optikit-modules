"""
Optical model for UC2 module: lens-pos-1x1
Thorlabs LA1131-A — Plano-convex, f=50mm, Ø25.4mm, N-BK7

UUID: opt-a1b2c3d4-lens-pcx-50mm
Module UUID: a1b2c3d4-e5f6-7890-abcd-ef1234567890

This script can be run standalone for quick analysis or imported
by OptiKit/Optiland integration scripts.

Usage:
    python model.py                    # Draw lens + spot diagram
    python model.py --save output.json # Export Optiland JSON
"""

import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants for this part (from Thorlabs LA1131-A datasheet)
# ---------------------------------------------------------------------------
PART = {
    "vendor": "Thorlabs",
    "sku": "LA1131-A",
    "uuid": "opt-a1b2c3d4-lens-pcx-50mm",
}

LENS_PARAMS = {
    "focal_length_mm": 50.0,
    "diameter_mm": 25.4,
    "radius_convex_mm": 25.8,         # R2 (convex surface)
    "radius_plano_mm": float("inf"),   # R1 (plano surface)
    "center_thickness_mm": 5.3,
    "edge_thickness_mm": 2.0,
    "material": "N-BK7",
    "material_catalog": "schott",
    "coating": "AR-A",
    "coating_range_nm": (350, 700),
    "design_wavelength_nm": 632.8,
    "clear_aperture_mm": 22.86,
}


def build_singlet():
    """
    Construct the Optiland Optic instance for this lens.

    Returns:
        optiland.optic.Optic: Configured singlet lens system.
    """
    from optiland import optic

    lens = optic.Optic()

    # Surface 0: Object at infinity
    lens.add_surface(index=0, radius=np.inf, thickness=np.inf)

    # Surface 1: Convex surface (light enters here)
    lens.add_surface(
        index=1,
        radius=LENS_PARAMS["radius_convex_mm"],
        thickness=LENS_PARAMS["center_thickness_mm"],
        material=("N-BK7", "schott"),
        is_stop=True,
    )

    # Surface 2: Plano surface (light exits here)
    # Thickness = approximate back focal length for collimated input
    lens.add_surface(
        index=2,
        radius=np.inf,
        thickness=44.7,  # approximate BFL
    )

    # Surface 3: Image plane
    lens.add_surface(index=3)

    # Aperture: entrance pupil diameter = lens diameter
    lens.set_aperture(aperture_type="EPD", value=LENS_PARAMS["diameter_mm"])

    # Fields: on-axis for a singlet
    lens.set_field_type(field_type="angle")
    lens.add_field(y=0.0)

    # Wavelengths: Fraunhofer F, d, C lines
    lens.add_wavelength(value=0.4861)                   # F-line
    lens.add_wavelength(value=0.5876, is_primary=True)  # d-line
    lens.add_wavelength(value=0.6563)                   # C-line

    return lens


def analyze(lens):
    """Run basic analyses on the lens and print results."""
    from optiland.analysis import SpotDiagram

    print("=" * 60)
    print(f"  {PART['vendor']} {PART['sku']} — Plano-Convex Singlet")
    print(f"  f = {LENS_PARAMS['focal_length_mm']} mm, "
          f"Ø{LENS_PARAMS['diameter_mm']} mm, "
          f"{LENS_PARAMS['material']}")
    print("=" * 60)

    lens.info()

    print("\n--- Spot Diagram ---")
    spot = SpotDiagram(lens)
    spot.view()


def save_optiland_json(lens, filepath="optiland.json"):
    """Export the lens to Optiland's native JSON format."""
    from optiland.fileio import save_optiland_file
    save_optiland_file(lens, filepath)
    print(f"Saved Optiland JSON to: {filepath}")


# ---------------------------------------------------------------------------
# Ray-transfer matrix model (thin-lens approximation)
# For quick calculations without importing optiland
# ---------------------------------------------------------------------------
def thin_lens_matrix(f_mm):
    """Return the 2×2 ray-transfer matrix for a thin lens."""
    return np.array([
        [1.0,     0.0],
        [-1.0/f_mm, 1.0],
    ])


def free_space_matrix(d_mm):
    """Return the 2×2 ray-transfer matrix for free-space propagation."""
    return np.array([
        [1.0, d_mm],
        [0.0, 1.0],
    ])


def propagate(ray, matrices):
    """
    Propagate a ray [height, angle] through a sequence of matrices.

    Args:
        ray: np.array([height_mm, angle_rad])
        matrices: list of 2x2 numpy arrays (applied left to right)

    Returns:
        np.array([height_mm, angle_rad]) after propagation
    """
    result = ray.copy()
    for M in matrices:
        result = M @ result
    return result


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Optical model for UC2 lens-pos-1x1 module"
    )
    parser.add_argument(
        "--save", type=str, default=None,
        help="Export Optiland JSON to this filepath"
    )
    parser.add_argument(
        "--matrix-only", action="store_true",
        help="Only print thin-lens matrix (no optiland dependency)"
    )
    args = parser.parse_args()

    if args.matrix_only:
        M = thin_lens_matrix(LENS_PARAMS["focal_length_mm"])
        print(f"Thin-lens matrix (f={LENS_PARAMS['focal_length_mm']} mm):")
        print(M)
    else:
        lens = build_singlet()
        if args.save:
            save_optiland_json(lens, args.save)
        else:
            analyze(lens)
