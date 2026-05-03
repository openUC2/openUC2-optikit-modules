# User Manual — Laser 635 nm (CPS635R) 1x1

## Before You Start

Make sure you have:
- One UC2 cube (v4 or later)
- One 3D-printed CPS laser holder (PLA is fine - laser dissipates << 1 W)
- One Thorlabs CPS635R laser module
- One 5 V DC power supply (>= 200 mA)
- Laser safety glasses rated for 635 nm (OD 4+)

## Installation

1. **Wear laser safety glasses** before powering anything on.
2. **Press-fit the CPS635R into the laser holder.** The holder uses a cylindrical bore (11.05 mm) for self-centring. The laser body should slide in with light pressure; do not force it.
3. **Connect the 5 V leads.** Red = +5 V, black = ground. The CPS635R has built-in current limiting - no external resistor required.
4. **Slide the assembly into the UC2 cube.** The beam exits from the +X face along the optical axis.
5. **Power on.** The laser warms up to within 5.0% of its final power within 5 minutes.

## Software

With the ImSwitch driver loaded (`software/imswitch/driver.py`), the laser can be controlled programmatically:

```python
controller.lasers["Laser_635"].setEnabled(True)   # turn on
controller.lasers["Laser_635"].setValue(2.5)      # 2.5 mW
```

## Safety

- **Class 3R** - direct intrabeam viewing is hazardous. Always wear OD 4+ safety glasses for 635 nm.
- Never look into the cube along the +X axis when powered.
- Use a beam dump downstream of the last optical element when not imaging.


## Troubleshooting

See `troubleshooting.md` for common issues.
