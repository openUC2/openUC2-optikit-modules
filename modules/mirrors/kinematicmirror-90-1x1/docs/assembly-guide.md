# Assembly Guide — Kinematic Mirror (90 deg) 1x1

## Internal Assembly (Production)

### Bill of Materials

See `cad/bom.yaml` for the full BOM.

### Steps

1. **Print the mount adapter.** Use `production/printing.yaml` settings. Recommended: PLA or PETG, 0.2 mm layer height, 80 % infill, 4 walls.
2. **Quality check the print.** The cradle must grip the POLARIS-K1 tube firmly without warping. Test-fit before any final assembly.
3. **Mount the mirror.** Insert the BB1-E02 into the POLARIS-K1 cradle. Tighten the retaining clip with the smallest necessary torque.
4. **Attach the mount to the adapter.** Slide the POLARIS-K1 into the adapter cradle, micrometer screws facing outward.
5. **Install into the UC2 cube.** Push the assembled adapter into the cube along the optical axis channel until seated.
6. **Initial alignment.** Center the mirror visually using a calibrated beam (e.g., He-Ne or low-power laser pointer through the input port). Walk the spot to the centre of the output port using the two micrometers.
7. **Label.** Apply the module label or QR code.

### Quality Checks

- [ ] Mirror is firmly held in the POLARIS-K1 cradle
- [ ] Both micrometer screws can be turned through their full range
- [ ] No fingerprints or dust on the mirror surface
- [ ] Beam folds approximately to the labelled output face

## External Assembly (User / Repair)

For field replacement, follow the same steps in reverse to disassemble, then re-assemble using a fresh consumable. The 3D-printed adapter is the wear item - typically lasts 50+ insertions before needing replacement.
