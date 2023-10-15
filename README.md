# РИСАТЕНО
 


РИСАТЕНО (__RISATENO__) - created as a rethinking of [ARTSEY](https://artsey.io/) for the Russian language. 10 keys, two for each finger.

The name is made up of letters on the main layer. The letters on the base layer are selected according to the [frequency](https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C).

Gerber files and stl models can be downloaded in [releases](https://github.com/aroum/PNCATEHO/releases).

[Post on reddit with photos](https://www.reddit.com/r/ErgoMechKeyboards/comments/r8novj/%D1%80%D0%B8%D1%81%D0%B0%D1%82%D0%B5%D0%BD%D0%BE_risateno_10_key_chord_keyboard/)

![front](pcb/renders/front.png)

# Features
* 10 keys, Kailh Choc V1 switches
* Choc spacing
* Direct pins 
* Wireless(optional)
* Per switch RGB(optional)
* Power switch for wireless controllers(optional)
* Two halves inscribed in 100x100 mm(optional)
* Three mounting screws
* One PCB for right and left versions

# Inspiration

* [ARTSEY](https://artsey.io/)
* [The Paintbrush](https://github.com/artseyio/thepaintbrus)
* [Helix](https://github.com/MakotoKurauchi/helix)
* [wakizashi](https://klava.wiki/hypha/%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/%D0%B2%D0%B0%D0%BA%D0%B8%D0%B4%D0%B7%D0%B0%D1%81%D0%B8) (saw after the release of PNCATEHO)


# Options
РИСАТЕНО can be used with [nRFMicro](https://github.com/joric/nrfmicro) or [nice!nano](https://nicekeyboards.com/nice-nano/) and 301230 batteries for wireless mode. It can also be used as a split keyboard for two hands with wireless communication of the halves.



From version 0.2+ the PCB are double-sided, one PCB can be used for the right and left variant. On the left version, the controller is soldered components down, on the right, components up.

# Layouts
РИСАТЕНО designed for one-handed chord typing, the layout [here](http://www.keyboard-layout-editor.com/#/gists/019e404b4ab5db93cd75010ad90777a4). 

The original idea was to create a compact keyboard for chord typing, but it can also be used as a macro pad.

When using two halves of РИСАТЕНО connected via Bluetooth, you can use the [Kladenets layout](https://ibnteo.github.io/kladenets/).


# BOM

| Item                                                                   | Quantity | Remarks                              |
| ---------------------------------------------------------------------- | -------: | ------------------------------------ |
| [proMicro](https://aliexpress.ru/item/32840365436.html)                | 1        | or any other compatible controller   |
| [Kailh Choc V1](https://aliexpress.ru/item/32959996455.html)           | 10       | switches                             |
| [Keycaps](https://aliexpress.ru/item/33026798318.html)                 | 10       | 1U                                   |
| [YS-SK6812MINI-E](https://aliexpress.ru/item/4000475685852.html)       | 10       | RGB leds                             |
| [Magnets](https://aliexpress.ru/item/1005002757445161.html)            | 2-6      | disc 7x2 mm (for case)               |
| [Bumpers](https://aliexpress.ru/item/4001188580018.html)               | 7        | 5x2 mm                               |
| [Sockets PH3.5](https://aliexpress.ru/item/32899635835.html)           | 12x2     | for controller                       |
| [SMD button 3x4x2mm](https://aliexpress.ru/item/1005003812819985.html) | 1        | for reset                            |
| [MSK-12C02](https://aliexpress.ru/item/1005001398386692.html)          | 1        | Power switch  (wireless only)        |
| [301230](https://aliexpress.ru/item/32732458079.html)                  | 1        | Battery  (wireless only)             |


# Build guide
1. Solder the controller sockets
2. Solder the power switch (wireless only)
3. Solder the reset button
4. Solder the battery (only for wireless version)
5. Solder the pins into the controller (On the left version, the controller is soldered components down, on the right, components up.)
6. Solder 10 Kailh Choc V1 switches (optionally install plate)
7. Solder 10 LEDs (RGB version only)
8. Put the keycaps on the switches
9. Stick Bumpers or place the keyboard in the case
10. Insert controller into sockets
11. Flash the bootloader (see the official manual for the controller)
12. Flash the firmware (see the official manual for the controller)

[Soldering Tutorial for Beginners](https://mightyohm.com/files/soldercomic/FullSolderComic_EN.pdf) ([RU version](https://sho0.neocities.org/downloads/komiks_payat_prosto.pdf))
