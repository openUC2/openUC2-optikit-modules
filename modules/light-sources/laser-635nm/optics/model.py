"""
Optical model for UC2 module: laser-635nm
Thorlabs CPS635R - Collimated 635 nm laser diode module, 4.5 mW class-3R, integrated drive electronics

UUID: opt-e5f6a7b8-laser-cps635r
Module UUID: e5f6a7b8-c9d0-1234-ef01-567890123456
"""

import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants for this part
# ---------------------------------------------------------------------------
PART = {
    "vendor": "Thorlabs",
    "sku":    "CPS635R",
    "uuid":   "opt-e5f6a7b8-laser-cps635r",
}

LASER_PARAMS = {
    "wavelength_nm":        635.0,
    "power_mW":             4.5,
    "beam_diameter_mm":     3.5,
    "beam_divergence_mrad": 0.5,
    "polarization":         "linear",
    "laser_class":          "3R",
}


def build_source():
    """Construct an Optiland Optic instance with this laser as the source."""
    from optiland import optic

    s = optic.Optic()
    s.add_surface(index=0, radius=np.inf, thickness=0.0, is_stop=True)
    s.add_surface(index=1)
    s.set_aperture(aperture_type="EPD", value=LASER_PARAMS["beam_diameter_mm"])
    s.set_field_type(field_type="angle")
    s.add_field(y=0.0)
    wl_um = LASER_PARAMS["wavelength_nm"] / 1000.0
    s.add_wavelength(value=wl_um, is_primary=True)
    return s


def gaussian_beam_waist_mm(M_squared: float = 1.2) -> float:
    wl_mm = LASER_PARAMS["wavelength_nm"] * 1e-6
    theta_rad = LASER_PARAMS["beam_divergence_mrad"] * 1e-3
    return (M_squared * wl_mm) / (np.pi * theta_rad)


def rayleigh_range_mm(M_squared: float = 1.2) -> float:
    w0 = gaussian_beam_waist_mm(M_squared)
    wl_mm = LASER_PARAMS["wavelength_nm"] * 1e-6
    return np.pi * w0 ** 2 / (M_squared * wl_mm)


def power_density_W_per_cm2() -> float:
    area_cm2 = np.pi * (LASER_PARAMS["beam_diameter_mm"] / 2 / 10) ** 2
    return (LASER_PARAMS["power_mW"] * 1e-3) / area_cm2


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
    parser = argparse.ArgumentParser(description="Optical model for laser-635nm")
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
