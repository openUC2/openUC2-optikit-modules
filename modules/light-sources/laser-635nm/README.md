# Laser 635 nm (CPS635R) - 1x1 UC2 Module

| Property | Value |
|----------|-------|
| **Module ID** | `laser-635nm` |
| **UUID** | `e5f6a7b8-c9d0-1234-ef01-567890123456` |
| **Category** | Light-source |
| **Grid Size** | 1x1 (50 mm x 50 mm x 50 mm) |
| **Scenario** | 2 - Generic Part (template-driven) |
| **Version** | 1.0.0 |

## Overview

Provides a collimated red beam along the cube +X axis. The CPS series integrates the laser diode, a collimating lens, and a constant-current driver into a single 11 mm package. A 5 V external supply drives it; no separate controller is needed.

The default part is the **Thorlabs CPS635R**.

## Quick Specs

- **Wavelength:** 635.0 nm (+/- 10.0 nm)
- **Output power:** 4.5 mW (stability +/- 5.0%)
- **Beam diameter:** 3.5 mm at exit
- **Divergence:** 0.5 mrad (full angle)
- **Polarization:** linear
- **Laser class:** 3R
- **Drive:** 5.0 V DC, 80 mA

## Optical / Data Ports

| Port | Face | Type | Description |
|------|------|------|-------------|
| `port-optical-out` | +X | Optical | Collimated 635 nm beam, ~3.5 mm dia |
| `port-power-in` | -X | Power | 5 V DC input via 2-pin connector |

## OptiKit Registry Mapping

This module appears in the OptiKit exporter database (`modules_updated.csv`)
with the following resolved fields: `opticalKind=ideal`, `idealKind=source`, `wavelength_nm=635.0`, `wavelengthBandwidth_nm=1.0`, `power_mW=4.5`, `beamDiameter_mm=3.5`.

When `optikit_exporter.module_registry.ModuleRegistry.from_csv()` runs and
finds this folder via `--modules`, the per-module `optics/optiland.json`
below replaces the CSV row's `kind: ideal` with `kind: optiland_json` -
the surface group from this folder becomes the source of truth.

## References

- **Optiland model:** `optics/optiland.json` -> [openuc2-optiland-models](https://github.com/openuc2/openuc2-optiland-models) `opt-e5f6a7b8-laser-cps635r`
- **CAD assembly:** `ASS - 2023 - LSRCPS635R - V02.iam` -> [openuc2-cad-modules](https://github.com/openuc2/openuc2-cad-modules) `cad-e5f6a7b8-laser-cps635r`
- **Vendor:** [Thorlabs CPS635R](https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS635R)

## File Structure

```
laser-635nm/
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

Drag this module from the **Fluorescence** group in the Part
Library onto the grid. Connect it to other modules via the ports listed
above. Adjustments shown under `parameters.variable` in `module.yaml`
are exposed to the user at runtime via the ImSwitch UI.

## License

Hardware: CERN-OHL-S-2.0 | Documentation: CC-BY-SA-4.0
