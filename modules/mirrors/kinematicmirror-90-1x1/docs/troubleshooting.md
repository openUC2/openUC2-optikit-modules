# Troubleshooting — Kinematic Mirror (90 deg) 1x1

## Q: The reflected beam doesn't hit the next module

**A:** Walk the beam onto the target using the two POLARIS-K1 micrometers. One full turn moves the beam by ~7 mm at 200 mm distance. If the misalignment is greater than the micrometer range (+/-4 deg), check that the mirror is oriented correctly relative to the labelled output face.

## Q: The mirror appears to wobble

**A:** The POLARIS-K1 retaining clip may be too loose. Tighten the retaining screw on the mirror cradle. Do not over-tighten - this can warp the mirror surface and degrade the wavefront.

## Q: I see ghost reflections / multiple spots

**A:** Either the beam is hitting the substrate's back surface (which has no AR coating on bare BB1-E02 mirrors), or there is a stray reflection from another optical element. Verify the mirror is oriented coating-side toward the beam.

## Q: I need a different wavelength range

**A:** Swap the BB1-E02 for another mirror in the BB1-E0x series. The POLARIS-K1 mount and the printed adapter are wavelength-agnostic. Update `metadata.sku` in `module.yaml` and the `wavelength_range_nm` in `parameters.static`.

## Q: The Optiland simulation predicts the beam at the wrong position

**A:** Verify that:
1. `mirrorAngle_deg` in the CSV matches the physical mirror orientation (45 vs 90)
2. The CSV propagation-axis lookup matches your layout
3. The `rxOffset_deg` / `ryOffset_deg` values reflect your final aligned state
