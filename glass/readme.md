# glass
The modern era of PNCATEHO development. It differs from the Stone era in that it supports hot-swappable keys and ChocV1/V2, MK Dose, and MX switches. It also uses closed cases and a new design approach by turtle_bazon.

## v5
An updated version of the PCB by turtle_bazon. It retains the core features of the Stone era, while adding support for Choc V2, as well as hot-swappable switches, an enclosed case, and a PCB with a more refined design.

![preview](../doc/img/preview/v5_preview.jpg)

<p align="center">
  <a href="case/v5/">Case | </a>
  <a href="build_v5.md">Build Guide</a>
</p>

### Features
* 10 keys, Kailh Choc **V1/V2** switches
* **Hot-Swap Socket**
* MX spacing
* Direct pins 
* Three mounting screws
* One PCB for right and left versions
* Wireless (optional)
* Per switch RGB (optional)
* Power switch for wireless controllers (optional)
* Two halves placed on one 100x100mm pcb (optional)

### PCB
The current PCB version is 0.5.2. For manufacturing, it is recommended to use 100×100 mm Gerber files. This way, 5 boards become 10 halves (with an extra cute keychain in between).

<p align="center">
  <img src="../doc/img/pcb/glass/v5_left.svg" width="45%">
  <img src="../doc/img/pcb/glass/v5_right.svg" width="45%">
</p>

### Case
To assemble the case, you need to print the following files:

* PNCATEHO_MK_DOSE-case-bottom-left - top part of the case
* PNCATEHO_MK_DOSE-case-top-left.step -  bottom part of the case
* PNCATEHO_MK_DOSE-reset-button-pusher.step - reset button actuator
* PNCATEHO_MK_DOSE-case-top-cover-blank-left - controller cover


There are also different versions of the controller cover with katakana or lp. Additionally, the case [directory](../glass/case/MK_DOSE) includes an editable FreeCAD file: **PNCATEHO_v5.FCStd**.

### BOM
| Item                                 | Quantity | Remarks                                      |
| ------------------------------------ | -------: | -------------------------------------------- |
| nice!nano                            |        1 | or any other pro micro compatible controller |
| Kailh Choc V1/2                      |       10 | switches                                     |
| Hot swap sockets                     |       10 | CPG135001S30                                 |
| YS-SK6812MINI-E                      |       10 | RGB leds                                     |
| Machine Pin Socket with 2.54mm pitch |     12x2 | for controller                               |
| RGB Led pin or brass wire            |     12x2 | for pin header                               |
| SMD button 3x4x2mm                   |        1 | for reset                                    |
| MSK-12C02                            |        1 | power switch  (wireless only)                |
| 301230 3.7v li-po                    |        1 | battery  (wireless only)                     |
| Silicone rubber feet                 |        5 | 10x2 mm                                      |
| M2х6 screw                           |        3 | for case                                     |
| Keycaps                              |       10 | 1U                                           |

## MK Dose
A version of the PCB designed for MK Dose format switches. It also supports standard MX switches. It differs by lacking per-switch backlighting, but includes indication using three SMD LEDs. Like V5, it features an enclosed case available in several variations.

![preview](../doc/img/preview/dose_preview.jpg)

<p align="center">
  <a href="case/MK_DOSE/">Case | </a>
  <a href="build_mkdose.md">Build Guide</a>
</p>

### Features
* 10 keys, MK Dose/MX switches
* 3 Led indication
* **Hot-Swap Socket**
* MX spacing
* Three mounting screws
* One PCB for right and left versions
* Wireless (optional)
* Power switch for wireless controllers (optional)
* Two halves placed on one 100x100mm pcb (optional)

### PCB

it is recommended to use 100×100 mm Gerber files. This way, 5 boards become 10 halves (with an extra cute keychain in between).

<p align="center">
  <img src="../doc/img/pcb/glass/mk_left.svg" width="45%">
  <img src="../doc/img/pcb/glass/mk_right.svg" width="45%">
</p>

### Case
To assemble the case, you need to print the following files:

* PNCATEHO_v5-bottom-case-left - top part of the case
* PNCATEHO_v5-top-case-left.step -  bottom part of the case
* PNCATEHO_v5-power-switch-pusher.step - power switch actuator
* PNCATEHO_v5-reset-button-pusher.step - reset button actuator
* PNCATEHO_v5-top-cover-left-blank.step - controller cover

There are also different versions of the controller cover with the **PNCATEHO** label in *ReggageOne* or *RubikMonoOne* fonts.
Additionally, the case [directory](../glass/case/v5) includes an editable FreeCAD file: **PNCATEHO_MK_DOSE.FCStd*.

### BOM
| Item                                 | Quantity | Remarks                                      |
| ------------------------------------ | -------: | -------------------------------------------- |
| nice!nano                            |        1 | or any other pro micro compatible controller |
| MK Dose or MX Swtich                 |       10 | switches                                     |
| Hot swap sockets                     | 10 or 20 | CPG151101S11                                 |
| Diode 1N4148W                        | 10 or 20 | for matrix                                   |
| 0603 led                             |        3 | for indication                               |
| 0603 1-10k resitsor                  |        3 | for led                                      |
| Machine Pin Socket with 2.54mm pitch |     12x2 | for controller                               |
| RGB Led pin or brass wire            |     12x2 | for pin header                               |
| SMD button 3x4x2mm                   |        1 | for reset                                    |
| BSI-10H                              |        1 | power switch  (wireless only)                |
| 301230 3.7v li-po                    |        1 | battery  (wireless only)                     |
| Silicone rubber feet                 |        5 | 8x2 mm                                       |
| m2х8 screw                           |        3 | for case                                     |
| Keycaps                              |       10 | 1U                                           |
