# Kinematic Mirror (45 deg) - 1x1 UC2 Module

| Property | Value |
|----------|-------|
| **Module ID** | `kinematicmirror-1x1` |
| **UUID** | `b2c3d4e5-f6a7-8901-bcde-f23456789012` |
| **Category** | Mirror |
| **Grid Size** | 1x1 (50 mm x 50 mm x 50 mm) |
| **Scenario** | 2 - Generic Part (template-driven) |
| **Version** | 1.0.0 |

## Overview

Folds an incoming optical beam by 90 degrees (mirror normal at 45 degrees to both ports). Two micrometer screws provide +/-4 deg of tilt about pitch and yaw axes for precise alignment.

The default part is the **Thorlabs POLARIS-K1 + BB1-E02**.

## Quick Specs

- **Fold angle:** 90.0 deg (mirror normal at 45.0 deg)
- **Diameter:** 25.4 mm (1 inch)
- **Reflectance:** > 99.0% over 400-750 nm
- **Surface flatness:** lambda/10
- **Tilt range:** +/- 4.0 deg on each axis
- **Tilt resolution:** 14.0 arcsec/turn (typical)

## Optical / Data Ports

| Port | Face | Type | Description |
|------|------|------|-------------|
| `port-optical-in` | +X | Optical | Incoming beam |
| `port-optical-out` | +Y | Optical | Reflected beam (90 deg fold) |

## OptiKit Registry Mapping

This module appears in the OptiKit exporter database (`modules_updated.csv`)
with the following resolved fields: `opticalKind=ideal`, `idealKind=mirror`, `diameter_mm=25.4`, `thickness_mm=6.0`, `material=mirror`, `mirrorAngle_deg=45.0`.

When `optikit_exporter.module_registry.ModuleRegistry.from_csv()` runs and
finds this folder via `--modules`, the per-module `optics/optiland.json`
below replaces the CSV row's `kind: ideal` with `kind: optiland_json` -
the surface group from this folder becomes the source of truth.

## References

- **Optiland model:** `optics/optiland.json` -> [openuc2-optiland-models](https://github.com/openuc2/openuc2-optiland-models) `opt-b2c3d4e5-mirror-45deg`
- **CAD assembly:** `ASS - 2022 - KMNT45D - V03.iam` -> [openuc2-cad-modules](https://github.com/openuc2/openuc2-cad-modules) `cad-b2c3d4e5-mirror-45deg`
- **Vendor:** [Thorlabs POLARIS-K1 + BB1-E02](https://www.thorlabs.com/thorproduct.cfm?partnumber=POLARIS-K1)

## File Structure

```
kinematicmirror-1x1/
├── module.yaml              # Master descriptor (this module)
├── README.md                # This file
├── docs/                    # Documentation
├── optics/                  # Optical models & coordinate systems
├── cad/                     # CAD files, exports, BOM
├── electronics/             # (empty - passive element)
├── firmware/                # (empty - no firmware)
├── software/                # ImSwitch integration notes
├── configurator/            # Icons and thumbnails for web UI
├── production/              # Print settings, supply chain
└── marketing/               # Photos, slides
```

## Usage in OptiKit

Drag this module from the **Mirrors** group in the Part
Library onto the grid. Connect it to other modules via the ports listed
above. Adjustments shown under `parameters.variable` in `module.yaml`
are exposed to the user at runtime through the cube's mechanical adjusters.

## License

Hardware: CERN-OHL-S-2.0 | Documentation: CC-BY-SA-4.0
