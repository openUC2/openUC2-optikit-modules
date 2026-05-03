# User Manual — USB Camera (HIK MV-CA013-21UC) 1x1

## Before You Start

Make sure you have:
- One UC2 cube (v4 or later)
- One 3D-printed C-mount adapter (PETG recommended for thread durability)
- One Hikrobot MV-CA013-21UC camera
- One USB3.2 Type-C cable (locking type recommended)
- 5 V power source (USB or external)

## Installation

1. **Screw the camera onto the C-mount adapter.** Hand-tight is sufficient - the C-mount thread is self-aligning.
2. **Insert the assembly into the UC2 cube.** Route the USB-C cable through the cutout on the -X face.
3. **Verify the sensor is centred** on the optical axis. Look through the +X face with a flashlight; the sensor should appear in the centre of the bore.
4. **Connect to the host PC** with the USB cable. Windows / Linux drivers are available from the Hikrobot website (MVS SDK).

## Software

ImSwitch is configured via `software/imswitch/config_snippet.json`. Drop this snippet into your ImSwitch setup file under the `detectors` key. The ImSwitch GUI will then expose exposure, gain, and ROI controls.

```python
controller.detectors["Camera_HIK_USB"].setExposure(20000)  # 20 ms
frame = controller.detectors["Camera_HIK_USB"].grabFrame()
```

## Cleaning

- Use a blower bulb to remove dust from the sensor
- Never touch the sensor surface directly - use a sensor swab if needed
- Cover the C-mount with the protective cap when not in use


## Troubleshooting

See `troubleshooting.md` for common issues.
