"""
Example: state and basic API for the camera-usb module.
"""

def acquire_frame(controller, exposure_us: int = 10000):
    """Snap one frame at the given exposure and return the numpy array."""
    controller.lasers["Laser_635"].setEnabled(True)
    controller.detectors["Camera_HIK_USB"].setExposure(exposure_us)
    frame = controller.detectors["Camera_HIK_USB"].grabFrame()
    controller.lasers["Laser_635"].setEnabled(False)
    return frame


camera_state = {
    "module_id": "camera-usb",
    "module_uuid": "d4e5f6a7-b8c9-0123-def0-456789012345",
    "grid_position": {"x": 6, "y": 3, "z": 0},
    "parameters": {
        "vendor": "Hikrobot",
        "sku": "MV-CA013-21UC",
        "exposure_us": 10000,
        "gain_db": 0.0,
        "pixel_pitch_um": 1.85,
    },
}


def get_module_state():
    return camera_state


if __name__ == "__main__":
    import json
    print(json.dumps(get_module_state(), indent=2))
