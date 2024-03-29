# pncateho

*A short description of the keyboard/project*

* Firmware Maintainer: [Mayorov Kirill](https://github.com/FT256) [@Mayoroffk](https://t.me/mayoroffk)

Make example for this keyboard (after setting up your build environment):

    make pncateho:vial

Flashing example for this keyboard:

    make pncatehom:vial:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the top left up key and plug in the keyboard
* **Physical reset button**: Briefly press the button on the PCB
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
