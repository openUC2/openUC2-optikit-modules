# Assembly Guide — Laser 635 nm (CPS635R) 1x1

## Internal Assembly (Production)

### Bill of Materials

See `cad/bom.yaml` for the full BOM.

### Steps

1. **Print the laser holder.** PLA, 0.2 mm layers, 80 % infill, 4 walls.
2. **Quality check the print.** The 11 mm bore must be a slight press-fit on the CPS body. If too tight, ream lightly with a 11.0 mm drill bit.
3. **Solder the power leads.** Red wire to +5 V terminal, black to ground. Use heat shrink to insulate.
4. **Insert the laser** into the holder. Push gently along the optical axis until the laser body seats against the internal stop.
5. **Install into the UC2 cube.** Beam exit on +X face.
6. **Smoke test.** With safety glasses on, briefly apply 5 V. Verify a clean red dot on a target ~1 m away.

### Quality Checks

- [ ] Laser body seated against internal stop (no axial play)
- [ ] Beam exits perpendicular to +X cube face
- [ ] Beam diameter ~3.5 mm at exit
- [ ] No visible flicker or beating in the spot (indicates loose connection)

## External Assembly (User / Repair)

For field replacement, follow the same steps in reverse to disassemble, then re-assemble using a fresh consumable. The 3D-printed adapter is the wear item - typically lasts 50+ insertions before needing replacement.
