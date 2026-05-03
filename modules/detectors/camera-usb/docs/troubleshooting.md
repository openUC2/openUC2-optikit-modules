# Troubleshooting — USB Camera (HIK MV-CA013-21UC) 1x1

## Q: The image is dark / saturated

**A:** Adjust the exposure time and gain via the ImSwitch GUI or `controller.detectors[...].setExposure(...)`. Default exposure is 10 ms; try 1-100 ms to bracket your scene.

## Q: The camera doesn't enumerate

**A:** Check that:
1. USB3 Vision drivers are installed (Hikrobot MVS SDK on Windows / Linux)
2. The USB cable is rated for USB3 (USB2 cables won't deliver enough bandwidth)
3. The host port is USB3 (blue connector, or marked SS / 3.0)
4. The PC's user has access permissions to the camera (Linux: udev rules)

## Q: Frame rate is lower than expected

**A:** Lower the bit depth (8 vs 12), reduce the ROI to a smaller window, or reduce the exposure time. Cable bandwidth limits also apply - a 1 m USB3 cable supports the full 60 Hz; 5+ m active cables may cap at 30 Hz.

## Q: The image plane appears tilted

**A:** Verify the camera is seated flush against the C-mount adapter. A small wedge between the camera flange and the adapter introduces sensor tilt. Check the printed adapter for warping; reprint if necessary.

## Q: The Optiland simulation shows the wrong sensor size

**A:** Verify that `sensorWidth_mm` and `sensorHeight_mm` in `modules_updated.csv` match the actual sensor (11.25 x 7.03 mm for the MV-CA013-21UC). Vendor datasheets list the sensor format in inches - convert by diagonal = 16 x format_inches.
