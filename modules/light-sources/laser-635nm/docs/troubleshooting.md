# Troubleshooting — Laser 635 nm (CPS635R) 1x1

## Q: The laser doesn't turn on

**A:** Verify:
1. 5 V supply is delivering >= 200 mA (check with multimeter at the connector)
2. Polarity is correct (red = +5 V, black = ground)
3. The driver's `setEnabled(True)` was called and the GPIO line is high
4. The CPS body is not damaged (try the laser standalone, outside the cube)

## Q: The output power is unstable

**A:** The CPS635R warms up to within +/-5 % of its final power in ~5 minutes. For experiments requiring < 1 % stability, allow a 30 minute warmup and verify power with an external meter. Power supply ripple > 50 mV will also cause visible power fluctuations.

## Q: The beam isn't collimated

**A:** The CPS series has a fixed collimator - there is no user adjustment. If the beam appears divergent or focused, the laser may be damaged internally. Check beam diameter at 1 m and 2 m; difference should be < 1 mm for a working unit.

## Q: The wavelength seems wrong

**A:** Diode lasers shift wavelength with temperature (~0.25 nm/C). At room temperature the CPS635R typically lases between 632-642 nm. For spectroscopy applications, measure the actual wavelength with a calibrated spectrometer and update `parameters.static.wavelength_nm` in `module.yaml`.

## Q: The Optiland simulation uses the wrong wavelength

**A:** Verify that `wavelength_nm` in `modules_updated.csv` matches the physical laser. The exporter's `_wavelengths_from_chain()` reads this value and converts to um before passing it to Optiland's `wavelengths.add()`.
