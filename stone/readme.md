# STONE
The standard version of PNCATEHO from the Stone era. Supports per-key backlighting, the option to use a wireless controller with an external power switch and reset button, and an open case. It does not support hot-swapping switches and only supports Choc V1.

![preview](../doc/img/preview/stone_preview.jpg)

<p align="center">
  <a href="case/case_v4.stp">Case | </a>
  <a href="build.md">Build Guide</a>
</p>

## V0.3

### Features
* 10 keys, Kailh Choc V1 switches
* Choc spacing
* Direct pins 
* Three mounting screws
* One PCB for right and left versions
* Wireless (optional)
* Per switch RGB (optional)
* Power switch for wireless controllers (optional)
* Two halves placed on one 100x100mm pcb (optional)


### PCB
There are several versions of the PCB. In version 0.3, the right half has an error in the LED footprints, so the backlighting can only be installed facing downward. This issue, along with other minor ones, was fixed in version 0.4.

For manufacturing, it is recommended to use 100×100 mm Gerber files. This way, 5 boards become 10 halves (5 right and 5 left).

### Case
In the case directory, there are two STEP files. case_v4.stp does not have cutouts for rubber feet, while case_v4_flex.stp includes 7 cutouts for rubber feet.

<p align="center">
  <img src="../doc/img/pcb/stone/stone_left.svg" width="45%">
  <img src="../doc/img/pcb/stone/stone_right.svg" width="45%">
</p>

### Plate
No plate is needed for choc, but if you want you can order PCB or laser cut. These don't fit version 3 boards because you can't add screw cutouts.

### BOM
| Item                 | Quantity | Remarks                            |
| -------------------- | -------: | ---------------------------------- |
| nice!nano            |        1 | or any other compatible controller |
| Kailh Choc V1        |       10 | switches                           |
| Keycaps              |       10 | 1U                                 |
| YS-SK6812MINI-E      |       10 | RGB leds                           |
| Magnets              |      2-6 | disc 7x2 mm (for case)             |
| Sockets PH5.0mm      |     12x2 | for controller                     |
| SMD button 3x4x2mm   |        1 | for reset                          |
| MSK-12C02            |        1 | power switch  (wireless only)      |
| 301230 3.7v li-po    |        1 | battery  (wireless only)           |
| Silicone rubber feet |        7 | 5x2 mm                             |
| M2 nuts              |        3 | for case v3+                       |
| M2x4 sqrews          |        3 | for case v3+                       |

## 3D
![preview](../doc/img/preview/3d.jpg)

### Case
The case folder contains a STEP file. The controller, circuitry, and mounting method are entirely up to you.
