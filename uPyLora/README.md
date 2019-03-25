# uPyLora for nRF52
nRF52 using MicroPython meets LoRa.

# Setup
* `LoRaPingPong.py`: sends ping-pong messages between the nodes (bidirectional communication)
* `LoRaReceiver.py` and `LoraSender.py`: unidirectional communication between the nodes (Note: deploy the `LoRaReceiver.py` on one node and the `LoraSender.py` on another node). 

The 

# Hardware
* [Dragino Arduino Shield v1.4 915Mhz](http://www.dragino.com/products/module/item/102-lora-shield.html) board.

## Note ## 
On Dragino board, for [SV2 SV3 SV4], move jumper to left side (e.g. not the default settings).
This will enable SPI operations though [D13 D12 D11].  

## Note ##
On the PCA10040 or PCA10056 board, you will need to defeat the default Button and LED configuration. The simplest and surest way is to jumper the "SHIELD_DETECT" pin on the J5 header (ICSP) to a GND pin (see the PCA10040 schematic for details). This was necessary because the pins on J5 of the PCA10040 board were too long and didn't match many of the arduino shield boards.   The J5 pins were also trimmed (clipped) a bit to keep them from shorting on some arduino shield boards.  
In doing is, you will make the GPIO pins, which were used for Button/LED support, available for general use.  
If you want to re-establish Button/LED support, then you will have to use the IO-Extender (U7) to issues I2C commands.  The IO-Extender will respond to an I2C scan as device address [32].
### Suggestion ###   
Use wire-wrap technique to wire SHIELD_DETECT to one of the many GND pins. This allows you to easily undo the connection later. Wire-wrapping is a good method to form semi-permement connections on the PCA10040 board.

# Revision
* 0.1 first commit

# Licenses
* Apache 2.0

# References

 
