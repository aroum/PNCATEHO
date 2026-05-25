## Tool

For assembly, you will need a soldering iron, flux, solder paste, tweezers, and either a hot air gun or a hot plate. For convenience, it is also recommended to have a microscope to check for solder bridges and a stencil for applying the paste.

## IBOM

<p align="center">
  <a href="https://htmlpreview.github.io/?https://github.com/inpudiy/PNCATEHO/blob/master/light/welcome/doc/ibom.html" style="text-decoration: none;">IBOM |</a> 
  <a href="doc/schematic.pdf" style="text-decoration: none;"> Schematic PDF</a>
</p>

Using the links above, go to the page with the interactive BOM. When you hover over a component or a footprint, a pair will be highlighted the component and the location where it needs to be installed. For resistors, capacitors, and fuses, polarity does not matter. For all other components, use the markings on both the component and the PCB, matching them accordingly.

![ibom](../../../doc/img/build/light/welcome/ibom.png)

## Led

Find the side of the LED marked in green, and rotate that side inward toward the bracket on the PCB, as shown in the photo.

![diode](../../../doc/img/build/light/welcome/diode_single.png)
![diode](../../../doc/img/build/light/welcome/diode_pcb.png)

## Flash and USBLC6-2SC6

There are small, barely noticeable dots in the corner of both components. Install them so that these dots align with the markings on the PCB.

![diode](../../../doc/img/build/light/welcome/esd.png)
![diode](../../../doc/img/build/light/welcome/flash.png)

## Crystal (Y1)

On the underside of the crystal oscillator, there is a pin with a cut corner. When placing it with the pins facing down, this corner should align with the marked corner on the PCB, as shown in the photo. Use either a hot air rework station or a hot plate. 

![quartz_single](../../../doc/img/build/light/welcome/quartz_single.png)
![quartz_pcb](../../../doc/img/build/light/welcome/quartz_pcb.png)

## RP2040

Tin the pads for installing the controller with a small amount of solder paste, and do the same with the controller itself. Make sure you’ve also tinned the side pins of the controller, and that there is only a minimal amount of solder on the central pad of both the PCB and the controller. If you apply too much paste in the center, the controller will sit too high above the board.

Then apply flux and place the controller, aligning the dot on the controller with the marking on the PCB. Personally, I pre-tin the contacts with a soldering iron, then place the controller using a hot plate and align it during the soldering process.

After soldering, remove the flux and inspect the side pins of the controller. For extra assurance, you can reapply flux and run a soldering iron with a small amount of solder paste along the edges of the controller. If you notice any obvious misalignment, reheat the solder joints and carefully adjust the component with tweezers.

![rp_foot](../../../doc/img/build/light/welcome/rp_foot.png)
![rp_bottom](../../../doc/img/build/light/welcome/rp_bottom.png)
![rp_side](../../../doc/img/build/light/welcome/rp_side.png)
![rp_top_pcb](../../../doc/img/build/light/welcome/rp_top_pcb.png)
![rp_side_pcb](../../../doc/img/build/light/welcome/rp_side_pcb.png)

## TYPE-C-31-M-12

Apply solder paste or solder with flux and go over the pads. Make sure that no contacts are shorted together. Also, be sure to flip the board and solder the through-holes the solder should flow fully inside and bond with the connector housing; otherwise, it can be easily broken off.

![rp_top_pcb](../../../doc/img/build/light/welcome/usb_top.png)
![rp_side_pcb](../../../doc/img/build/light/welcome/usb_bottom.png)

## Flashing

> [!WARNING]  
> Before connecting the board to your computer, visually inspect it: make sure all components are present, check for the absence of solder bridges between pins, and remove any excess solder, flux, or solder paste.

At the stage where everything is installed except the backlight, switches, connector, and control buttons, it’s a good time to flash the firmware so that further work is easier.

When you plug in the cable, a good sign is that the red 3.3V LED turns on. On first connection, the board should appear as a USB flash drive—copy the UF2 firmware file onto it.

After flashing, reconnect the board and check whether it is detected using Device Manager or lsusb.

If the board is not detected when connected, or stops being detected after flashing, return to the visual inspection stage. In 99.9% of cases, the issue is due to an incorrect component, wrong polarity, or poor connections between the pins and the PCB pads.

Start by applying flux everywhere and go over all components with a soldering iron and solder (or solder paste).

![pcb_power](../../../doc/img/build/light/welcome/pcb_power.png)
![pcb_flash](../../../doc/img/build/light/welcome/pcb_flash.png)
![pcb_mcu](../../../doc/img/build/light/welcome/pcb_mcu.png)


## WS2812B

> [!WARNING]  
> Disconnect the power supply before starting to solder the backlight.

After flashing, it’s time to install the backlight. On the diode, you’ll find an edge marked in green, and on the PCB there is a triangle indicating direction. Install the diode so that the green-marked edge faces the same direction as the triangle, as shown in the photo below.

Before soldering, tin the pads and apply flux. Heat the area using a hot air station or hot plate, then place the diode. Be careful using a soldering iron or tweezers can easily damage it, so handle it with care.

![2020_single](../../../doc/img/build/light/welcome/2020_single.png)
![2020_foot](../../../doc/img/build/light/welcome/2020_foot.png)
![2020_pcb](../../../doc/img/build/light/welcome/2020_pcb.png)

The data line of the LEDs is shown in the image below. If any part of the LEDs is not working, try re-soldering the first non-functioning LED in the chain.

![2020_path](../../../doc/img/build/light/welcome/2020_path.png)


## CPG1316S01D02-01

Before soldering the switches, it is recommended to check everything else first. Connect the keyboard and, using tweezers, short the switch pins one by one to test them.

If each pin registers a key press correctly when shorted, install the switches as shown in the photo and solder them in place using a hot air station and solder paste.

> [!WARNING]  
> Before installing the keycaps, make sure all switches are functioning properly, as they are almost impossible to remove without damaging the switch.

![switch](../../../doc/img/build/light/welcome/switch.jpg)

## JST and button (optional)

For quick flashing and access to 8 GPIO pins, you can install a JST connector and buttons.

![jst](../../../doc/img/build/light/welcome/jst.jpg)


## Congratulations

Congratulations you’ve assembled your РИСАТЕНО Welcome!

![welcome](../../../doc/img/build/light/welcome/welcome.jpg)