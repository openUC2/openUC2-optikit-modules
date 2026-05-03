"""
ImSwitch driver shim for camera-usb (Hikrobot MV-CA013-21UC).

Wraps the vendor SDK behind ImSwitch's DetectorManager interface.
"""
from __future__ import annotations
from typing import Any


class HikCamDriver:
    """Thin facade over MvCameraControl_class for ImSwitch."""

    MODULE_UUID = "d4e5f6a7-b8c9-0123-def0-456789012345"
    VENDOR = "Hikrobot"
    SKU = "MV-CA013-21UC"

    def __init__(self, properties: dict[str, Any]):
        self._props = properties
        self._handle = None

    def start(self) -> None:
        """Open the camera and apply initial settings."""
        # from MvCameraControl_class import MvCamera
        # self._handle = MvCamera(); self._handle.MV_CC_OpenDevice(...)
        raise NotImplementedError("plug in vendor SDK calls here")

    def stop(self) -> None:
        if self._handle is not None:
            # self._handle.MV_CC_CloseDevice()
            self._handle = None

    def set_exposure(self, exposure_us: int) -> None: ...
    def set_gain(self, gain_db: float) -> None: ...
    def set_roi(self, x: int, y: int, w: int, h: int) -> None: ...

    def grab_frame(self):
        """Return the most recent frame as a numpy array."""
        raise NotImplementedError
