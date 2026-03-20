# Assembly Guide — Lens (Positive) 1×1

## Internal Assembly (Production)

### Bill of Materials

| # | Part | Qty | Source |
|---|------|-----|--------|
| 1 | UC2 Cube v4 (IM) | 1 | In-house (injection molded) |
| 2 | Lens insert (3D-printed) | 1 | In-house (FDM/SLA) |
| 3 | Thorlabs LA1131-A lens | 1 | Thorlabs |

### Steps

1. **Print the lens insert.** Use `production/printing.yaml` settings. Recommended: PLA or PETG, 0.2 mm layer height, 80% infill.
2. **Quality check the print.** Verify the inner diameter fits the 25.4 mm lens with light friction. Remove any support material or stringing from the lens seat.
3. **Insert the lens.** Wear gloves or use lens tissue. Place the lens curved-side-first into the insert. It should sit flush against the retaining lip.
4. **Install into cube.** Slide the loaded insert into the UC2 cube along the optical axis channel.
5. **Label.** Apply the module label or QR code to the top face of the cube.

### Quality Checks

- [ ] Lens is centered (no visible offset when looking through the cube)
- [ ] Insert slides smoothly but does not rattle
- [ ] No fingerprints or debris on lens surfaces
- [ ] Convex surface faces the +X direction

## External Assembly (User / Repair)

If a user needs to replace a broken lens:

1. Push the insert out of the cube using a flat tool through the opposite face
2. Push the old lens out of the insert from the back
3. Clean the insert with compressed air
4. Insert the new lens (convex side first, toward the retaining lip)
5. Re-insert into cube and verify alignment
