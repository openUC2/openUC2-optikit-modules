"""
Example: state and basic API for the laser-635nm module.
"""

def pulse(controller, duration_s: float = 0.5, power_mW: float = 1.0):
    """Pulse the laser at a given power for a given duration."""
    import time
    laser = controller.lasers["Laser_635"]
    laser.setValue(power_mW)
    laser.setEnabled(True)
    time.sleep(duration_s)
    laser.setEnabled(False)


laser_state = {
    "module_id": "laser-635nm",
    "module_uuid": "e5f6a7b8-c9d0-1234-ef01-567890123456",
    "grid_position": {"x": 0, "y": 3, "z": 0},
    "parameters": {
        "vendor": "Thorlabs",
        "sku": "CPS635R",
        "wavelength_nm": 635.0,
        "power_setpoint_mW": 1.0,
        "enabled": False,
    },
}


def get_module_state():
    return laser_state


if __name__ == "__main__":
    import json
    print(json.dumps(get_module_state(), indent=2))
