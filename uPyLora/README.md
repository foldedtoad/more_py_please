# uPyLora for nRF52
nRF52 using MicroPython meets LoRa.

# Setup
* `LoRaPingPong.py`: sends ping-pong messages between the nodes (bidirectional communication)
* `LoRaReceiver.py` and `LoraSender.py`: unidirectional communication between the nodes (Note: deploy the `LoRaReceiver.py` on one node and the `LoraSender.py` on another node).  

# Hardware
* [Dragino Arduino Shield v1.4 915Mhz](http://www.dragino.com/products/module/item/102-lora-shield.html) board.

## Dragino Board Notes ## 
On Dragino board, for the [SV2 SV3 SV4] headers, move jumper to left side (e.g. not the default settings).
This will enable SPI operations though arduino-defined [D11 D12 D13] pins (PCA10040 pins [P0.23 P0.24 P0.25] respectively).  

## PCA10040 board Notes ##
On the PCA10040 or PCA10056 board, you will need to defeat the default Button and LED configuration. The simplest and surest way is to jumper the `SHIELD_DETECT` pin on the J5 header (ICSP) to a `GND` pin (see the PCA10040 schematic for details). This was necessary because the pins on J5 of the PCA10040 board were too long and didn't match many of the arduino shield boards. The J5 pins were also trimmed (clipped) a bit to keep them from shorting on some arduino shield boards.  

In doing the above wiring, the GPIO pins (by default assigned for Button/LED support) will be freed for general use.  
If you wish to re-establish Button/LED support, then you will need to use the IO-Extender (U7) to issues I2C commands to access the Button/LEDs.  The IO-Extender will respond to an I2C bus scan as device address [32]. This support was not provided in this project.

### Suggestion ###   
Use wire-wrap technique to wire `SHIELD_DETECT` to one of the many GND pins on the PCA10040 board. This allows you to easily undo the connection later. Wire-wrapping is a good method to form semi-permement connections on the PCA10040 board.

### PCA10040 Schematics ###
For PCA10040 schematic, download the zip file [here](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52-DK/Download#infotab), unzip it, and navigate to "*PCA10040-nRF52832 Bluetooth Smart,ANT,2.4GHz RF Development Board 1_2_1/Schematic_Layout pdf files*" directory: the schematic pdf file should be there.

## General Notes ##
There are a couple of Saleae Logic traces included. They show the initialization sequence and the send-runtime sequence. The free viewer is available [here](https://www.saleae.com/downloads) 

## Firmware Notes ##
The following changes were made to the default *mpconfigport.h* file
```
#define MICROPY_STACK_CHECK         (0)
#define MICROPY_PY_UBINASCII        (1)
#define MICROPY_PY_UCTYPES          (1)
```
    
### SPI Configuration ###
SPI and GPIO Config for Nordic PCA10040 and PCA10056 boards
```
SPI SS        P0.22
SPI SCK       P0.25
SPI MOSI      P0.23
SPK MISO      P0.24
LORA RESET    P0.20
LORA DIO0     P0.13
```

SPI controller 0 is configured. 

A SPI bus baudrate of 1MHz is configured.

# Revision
* 0.1 first commit

# Licenses
* Apache 2.0

# References 
