# USB Camera (HIK MV-CA013-21UC) - 1x1 UC2 Module

| Property | Value |
|----------|-------|
| **Module ID** | `camera-usb` |
| **UUID** | `d4e5f6a7-b8c9-0123-def0-456789012345` |
| **Category** | Detector |
| **Grid Size** | 1x1 (50 mm x 50 mm x 50 mm) |
| **Scenario** | 2 - Generic Part (template-driven) |
| **Version** | 1.0.0 |

## Overview

Records the image plane in a UC2 imaging chain. Sensor sits at the optical axis at z = 25 mm from the cube +X face. C-mount adapter projects 17.526 mm into the cube; the active sensor surface is recessed accordingly.

The default part is the **Hikrobot MV-CA013-21UC**.

## Quick Specs

- **Sensor:** 11.25 x 7.03 mm (6080 x 3800 px)
- **Pixel pitch:** 1.85 um
- **Color filter:** Bayer RGGB
- **Shutter:** global
- **Max frame rate:** 60 Hz at full resolution
- **Bit depth:** 12 bit
- **Interface:** USB3 Vision (USB3.1 Gen1)
- **Lens mount:** C-mount (1-inch 32 UN)

## Optical / Data Ports

| Port | Face | Type | Description |
|------|------|------|-------------|
| `port-optical-in` | +X | Optical | Optical input - beam focuses onto sensor at z=cube_center |
| `port-usb` | -X | Data | USB3 Vision (Type-C) - image data + camera control |

## OptiKit Registry Mapping

This module appears in the OptiKit exporter database (`modules_updated.csv`)
with the following resolved fields: `opticalKind=ideal`, `idealKind=detector`, `sensorWidth_mm=11.25`, `sensorHeight_mm=7.03`, `pixelPitch_um=1.85`, `sensorResolutionX_px=6080`.

When `optikit_exporter.module_registry.ModuleRegistry.from_csv()` runs and
finds this folder via `--modules`, the per-module `optics/optiland.json`
below replaces the CSV row's `kind: ideal` with `kind: optiland_json` -
the surface group from this folder becomes the source of truth.

## References

- **Optiland model:** `optics/optiland.json` -> [openuc2-optiland-models](https://github.com/openuc2/openuc2-optiland-models) `opt-d4e5f6a7-camera-usb-hik`
- **CAD assembly:** `ASS - 2023 - CAMHIK013 - V02.iam` -> [openuc2-cad-modules](https://github.com/openuc2/openuc2-cad-modules) `cad-d4e5f6a7-camera-usb-hik`
- **Vendor:** [Hikrobot MV-CA013-21UC](https://www.hikrobotics.com/en/machinevision/productdetail?id=15991)

## File Structure

```
camera-usb/
├── module.yaml              # Master descriptor (this module)
├── README.md                # This file
├── docs/                    # Documentation
├── optics/                  # Optical models & coordinate systems
├── cad/                     # CAD files, exports, BOM
├── electronics/             # Active electronics
├── firmware/                # (empty - no firmware)
├── software/                # ImSwitch integration (active driver + state mapping)
├── configurator/            # Icons and thumbnails for web UI
├── production/              # Print settings, supply chain
└── marketing/               # Photos, slides
```

## Usage in OptiKit

Drag this module from the **Cameras** group in the Part
Library onto the grid. Connect it to other modules via the ports listed
above. Adjustments shown under `parameters.variable` in `module.yaml`
are exposed to the user at runtime via the ImSwitch UI.

## License

Hardware: CERN-OHL-S-2.0 | Documentation: CC-BY-SA-4.0
