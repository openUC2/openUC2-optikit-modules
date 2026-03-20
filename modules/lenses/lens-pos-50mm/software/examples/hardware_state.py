"""
Example: Reading and recording the state of a lens-pos-1x1 module.

Since this is a passive element, "state" here means the metadata
that should be recorded alongside microscope data for reproducibility.

In a real ImSwitch session, this metadata would be automatically
captured and embedded in the OME-TIFF or experiment log.
"""

# Example state dictionary for this module
lens_state = {
    "module_id": "lens-pos-1x1",
    "module_uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "grid_position": {"x": 3, "y": 2, "z": 0},  # Position in UC2 grid
    "parameters": {
        "focal_length_mm": 50.0,
        "diameter_mm": 25.4,
        "material": "N-BK7",
        "coating": "AR-A",
        "vendor": "Thorlabs",
        "sku": "LA1131-A",
        "dz_offset_mm": 0.0,   # Manual adjustment recorded
    },
}


def get_module_state():
    """Return current state for metadata embedding."""
    return lens_state


def print_state():
    """Pretty-print the module state."""
    import json
    print(json.dumps(lens_state, indent=2))


if __name__ == "__main__":
    print_state()
