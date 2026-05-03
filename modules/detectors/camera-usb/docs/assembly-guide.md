# Assembly Guide — USB Camera (HIK MV-CA013-21UC) 1x1

## Internal Assembly (Production)

### Bill of Materials

See `cad/bom.yaml` for the full BOM.

### Steps

1. **Print the C-mount adapter.** Use PETG for thread durability.
2. **Re-tap the C-mount thread.** PETG holds the thread shape but a M25.4x0.794 (1-inch 32 UN) tap pass cleans up the printed thread for repeatable mounting.
3. **Mount the camera.** Screw the Hikrobot camera into the adapter, hand-tight.
4. **Route the USB cable.** Pass the USB-C cable through the cube wall cutout before final installation.
5. **Install into the UC2 cube.** Slide the assembled adapter in until the sensor is centered on the optical axis.
6. **Test.** Power up over USB, check that the camera enumerates as `MV-CA013-21UC` in the Hikrobot MVS viewer.

### Quality Checks

- [ ] Camera screws cleanly into the C-mount adapter
- [ ] Sensor visible and centered when looking through +X face
- [ ] USB cable strain-relieved at the cube wall
- [ ] Camera enumerates correctly in MVS viewer

## External Assembly (User / Repair)

For field replacement, follow the same steps in reverse to disassemble, then re-assemble using a fresh consumable. The 3D-printed adapter is the wear item - typically lasts 50+ insertions before needing replacement.
