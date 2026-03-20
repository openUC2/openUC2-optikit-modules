# Troubleshooting — Lens (Positive) 1×1

## Q: The image is blurry / not in focus

**A:** Check that the lens is oriented correctly (convex side toward the collimated beam source). Adjust the axial position of the insert within the cube (±2 mm range). If using a different wavelength than the design wavelength (632.8 nm), the focal length shifts due to dispersion — you may need to adjust spacing.

## Q: There are ghost reflections / back-reflections

**A:** The AR-A coating reduces reflections to < 0.5% per surface in the 350–700 nm range. If you are working outside this range, consider switching to a different coating variant (AR-AB for 400–1100 nm, AR-B for 650–1050 nm).

## Q: The lens rattles inside the cube

**A:** The insert may be slightly undersized due to 3D print shrinkage. Add a small piece of foam tape to the outside of the insert, or reprint with a 0.1 mm larger outer dimension.

## Q: The lens fell out of the insert

**A:** The friction fit may be too loose. Check the insert inner diameter — it should be 25.5 ± 0.1 mm for a 25.4 mm lens. If printing in PLA, try reducing the inner diameter by 0.1 mm in the parametric template.

## Q: I need a different focal length

**A:** This module is compatible with any Thorlabs LA-series 1-inch plano-convex lens. Swap the lens and update `module.yaml` with the new parameters. Use the `generate_from_template.py` script to regenerate the Optiland model automatically.

## Q: The Optiland simulation doesn't match reality

**A:** Verify that:
1. The correct glass catalog is being used (Schott N-BK7)
2. The wavelengths in your simulation match your actual source
3. The lens-to-image distance accounts for the cube wall thickness (2.5 mm per wall)
4. The `dz_mm` variable parameter is set to your actual insert position
