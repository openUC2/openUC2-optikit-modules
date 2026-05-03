"""
Example: state and basic API for the kinematicmirror-90-1x1 module.
"""

mirror_state = {
    "module_id": "kinematicmirror-90-1x1",
    "module_uuid": "c3d4e5f6-a7b8-9012-cdef-345678901234",
    "grid_position": {"x": 3, "y": 3, "z": 0},
    "parameters": {
        "vendor": "Thorlabs",
        "sku": "POLARIS-K1 + BB1-E02",
        "fold_angle_deg": 180.0,
        "rxOffset_deg": 0.0,
        "ryOffset_deg": 0.0,
    },
}


def get_module_state():
    """Return current state for metadata embedding."""
    return mirror_state


if __name__ == "__main__":
    import json
    print(json.dumps(get_module_state(), indent=2))
