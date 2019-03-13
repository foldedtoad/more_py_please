
LIS3DH accelerometer driver for Nordic nRF52 series demo boards (PCA100xx) 
Tested on Nordic PCA10040 dev board (nRF52832) with Micropython release 1.10.0

The accelerometer board is available from Adafruit "LIS3DH Triple-Axis Accelerometer (PRODUCT ID: 2809)
which was carried on a protoboard Adafruit "Proto Shield for Arduino" (PRODUCT ID: 2077).

The PCA10040 board follows the Arduino shield form-factor, so the protoboard plugs into the PCA10040.

The accelerometer board is wired to the PCA10040 board though the prototype board.
The wiring is as follows:
* Device SCL to protoboard SCL
* Device SDA to protoboard SDA
* Device CS to protoboard Vdd (note: selects for I2C I/F operations)
* Device 3V0 to protoboard Vdd
* Device GND to protoboard Gnd
* Device INT to protoboard 1 (analog in)
