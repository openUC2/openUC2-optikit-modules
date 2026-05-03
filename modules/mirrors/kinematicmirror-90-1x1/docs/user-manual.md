# User Manual — Kinematic Mirror (90 deg) 1x1

## Before You Start

Make sure you have:
- One UC2 cube (v4 or later)
- One 3D-printed kinematic mount adapter
- One Thorlabs POLARIS-K1 kinematic mount
- One Thorlabs BB1-E02 (or equivalent) 1-inch mirror
- Hex key set (for the POLARIS clamping screws)

## Installation

1. **Mount the mirror** in the POLARIS-K1 cradle. Tighten the retaining clip just enough to hold the mirror - over-tightening warps the surface.
2. **Slide the kinematic mount into the printed adapter.** Both micrometer screws must remain accessible from the cube exterior.
3. **Install into the cube.** Push the assembled adapter into the UC2 cube channel until it seats against the internal stops.
4. **Verify orientation.** For the 45 deg variant, the mirror's normal should bisect the +X (input) and +Y (output) faces. For the 90 deg variant, the mirror normal should be parallel to the cube +X axis.

## Alignment

Use the two POLARIS-K1 micrometers to walk the reflected beam onto the downstream module. With sub-arcsec resolution, a quarter-turn shifts the beam roughly 3.5 arcsec - enough for sub-pixel image-plane alignment over a 200 mm chain.

Record the final micrometer angles in `parameters.variable.rx_offset_deg` and `parameters.variable.ry_offset_deg` of `module.yaml` for reproducibility.


## Troubleshooting

See `troubleshooting.md` for common issues.
