# uPyLora
nRF52 using MicroPython meets LoRa.

# Setup
* `LoRaPingPong.py`: sends ping-pong messages between the nodes (bidirectional communication)
* `LoRaReceiver.py` and `LoraSender.py`: unidirectional communication between the nodes (Note: deploy the `LoRaReceiver.py` on one node and the `LoraSender.py` on another node). 

# Hardware
* [Dragino Arduino Shield v1.4 915Mhz](http://www.dragino.com/products/module/item/102-lora-shield.html) board.

## Note ## 
On Dragino board, for [SV2 SV3 SV4], move jumper to left side (e.g. not the default settings).
This will enable SPI operations though [D13 D12 D11].  

# Revision
* 0.1 first commit

# Licenses
* Apache 2.0

# References

 