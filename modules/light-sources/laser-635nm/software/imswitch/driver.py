"""
ImSwitch driver shim for laser-635nm (Thorlabs CPS635R).

The CPS-series lasers have no digital interface - the driver emits
a digital enable on a GPIO line. PWM on the same line gives crude
power modulation (10% to 100% linear).
"""
from __future__ import annotations


class GPIOLaserDriver:
    """Single-channel CPS laser controlled via a GPIO enable line."""

    MODULE_UUID = "e5f6a7b8-c9d0-1234-ef01-567890123456"
    VENDOR = "Thorlabs"
    SKU = "CPS635R"
    MAX_POWER_MW = 4.5

    def __init__(self, gpio_line: str = "GPIO17"):
        self._gpio_line = gpio_line
        self._enabled = False
        self._power_mW = 0.0

    def setEnabled(self, enabled: bool) -> None:
        self._enabled = bool(enabled)
        # gpio.write(self._gpio_line, 1 if enabled else 0)

    def setValue(self, power_mW: float) -> None:
        """Set output power in mW (0..MAX_POWER_MW)."""
        p = max(0.0, min(float(power_mW), self.MAX_POWER_MW))
        self._power_mW = p
        # duty = p / self.MAX_POWER_MW
        # gpio.pwm(self._gpio_line, duty=duty, freq_hz=10_000)

    def getValue(self) -> float:
        return self._power_mW

    def getEnabled(self) -> bool:
        return self._enabled
