# Lens (Positive) — 1×1 UC2 Module

| Property | Value |
|----------|-------|
| **Module ID** | `lens-pos-1x1` |
| **UUID** | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| **Category** | Lens |
| **Grid Size** | 1×1 (50 mm × 50 mm × 50 mm) |
| **Scenario** | 2 — Generic Part (template-driven) |
| **Version** | 1.0.0 |

## Overview

This module holds a plano-convex lens inside a standard UC2 cube. The default part is a **Thorlabs LA1131-A** — a 1-inch diameter, f = 50 mm, N-BK7 plano-convex lens with broadband AR coating (350–700 nm).

The cube insert is generated from the parametric `templates/lens/` template using the lens diameter and thickness as input parameters. Light enters through the convex surface on the +X face and exits through the plano surface on the −X face.

## Quick Specs

- **Focal length:** 50 mm (at 632.8 nm design wavelength)
- **Diameter:** 25.4 mm (1 inch)
- **Material:** N-BK7 (Abbe number 64.17)
- **Coating:** AR-A (350–700 nm, < 0.5% avg reflectance per surface)
- **Center thickness:** 5.3 mm
- **Radius of curvature:** 25.8 mm (convex side)

## Optical Ports

| Port | Face | Type | Description |
|------|------|------|-------------|
| `port-optical-in` | +X | Optical | Accepts collimated/diverging/converging beams |
| `port-optical-out` | −X | Optical | Outputs converging beam (for collimated input) |

## References

- **Optiland model:** `optics/optiland.json` → [openuc2-optiland-models](https://github.com/openuc2/openuc2-optiland-models) `opt-a1b2c3d4-lens-pcx-50mm`
- **CAD assembly:** `ASS - 2021 - CUBLEND40F50 - V04.iam` → [openuc2-cad-modules](https://github.com/openuc2/openuc2-cad-modules) `cad-a1b2c3d4-lens-pcx-50mm`
- **Vendor:** [Thorlabs LA1131-A](https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1131-A)

## File Structure

```
lens-pos-1x1/
├── module.yaml              # Master descriptor (this module)
├── README.md                # This file
├── docs/                    # Documentation
├── optics/                  # Optical models & coordinate systems
├── cad/                     # CAD files, exports, BOM
├── electronics/             # (empty — passive element)
├── firmware/                # (empty — passive element)
├── software/                # ImSwitch integration notes
├── configurator/            # Icons and thumbnails for web UI
├── production/              # Print settings, supply chain
└── marketing/               # Photos, slides
```

## Usage in OptiKit

Drag this module from the **Lenses** group in the Part Library onto the grid. Connect it to other modules via the ±X optical ports. The focal length can be changed by swapping the underlying part (edit `parameters.static.focalLength_mm` in `module.yaml` and regenerate from template).

## License

Hardware: CERN-OHL-S-2.0 | Documentation: CC-BY-SA-4.0
