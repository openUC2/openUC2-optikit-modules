"""
Optical model for UC2 module: camera-usb
Hikrobot MV-CA013-21UC - 1.3 MP color CMOS camera, 1.85 um pixels, USB3 Vision, C-mount thread

UUID: opt-d4e5f6a7-camera-usb-hik
Module UUID: d4e5f6a7-b8c9-0123-def0-456789012345
"""

import numpy as np
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants for this part
# ---------------------------------------------------------------------------
PART = {
    "vendor": "Hikrobot",
    "sku":    "MV-CA013-21UC",
    "uuid":   "opt-d4e5f6a7-camera-usb-hik",
}

DETECTOR_PARAMS = {
    "sensor_width_mm":        11.25,
    "sensor_height_mm":       7.03,
    "pixel_pitch_um":         1.85,
    "resolution_x_px":        6080,
    "resolution_y_px":        3800,
    "quantum_efficiency_pct": 72.0,
    "back_focal_distance_mm": 17.526,
}


def build_detector():
    """Construct an Optiland Optic instance terminating at this detector."""
    from optiland import optic

    d = optic.Optic()
    d.add_surface(index=0, radius=np.inf,
                  thickness=DETECTOR_PARAMS["back_focal_distance_mm"])
    d.add_surface(index=1, is_stop=True)
    diag = np.hypot(DETECTOR_PARAMS["sensor_width_mm"],
                    DETECTOR_PARAMS["sensor_height_mm"])
    d.set_aperture(aperture_type="EPD", value=diag)
    d.set_field_type(field_type="angle")
    d.add_field(y=0.0)
    d.add_wavelength(value=0.450)
    d.add_wavelength(value=0.550, is_primary=True)
    d.add_wavelength(value=0.650)
    return d


def pixels_per_mm() -> float:
    return 1000.0 / DETECTOR_PARAMS["pixel_pitch_um"]


def airy_disk_diameter_um(wavelength_nm: float, f_number: float) -> float:
    return 2.44 * (wavelength_nm * 1e-3) * f_number


def is_diffraction_limited(wavelength_nm: float, f_number: float) -> bool:
    airy = airy_disk_diameter_um(wavelength_nm, f_number)
    return airy >= 2 * DETECTOR_PARAMS["pixel_pitch_um"]


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
    parser = argparse.ArgumentParser(description="Optical model for camera-usb")
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
