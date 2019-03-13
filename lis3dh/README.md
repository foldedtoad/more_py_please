
# LIS3DH Accelerometer Driver using FIFO mode

STMicro LIS3DH accelerometer driver for Nordic nRF52 series demo boards (PCA100xx) 
Tested on Nordic PCA10040 dev board (nRF52832) with Micropython release 1.10.0

Datasheet: STMicro LIS3DH (DocID17530 Rev 2) "MEMS digital output motion sensor: ultra-low-power high-performance 3-axis "nano" accelerometer"

App Note:  AN3308 (DocID18198 Rev 3) "LIS3DH: MEMS digital output motion sensor ultra-low-power high-performance 3-axis “nano” accelerometer"

**NOTE:** The STM LIS2DH device should work without modifications. There may be other devices in the LISxyy series which work as well.

The accelerometer board is available from Adafruit "LIS3DH Triple-Axis Accelerometer (PRODUCT ID: 2809)
which was carried on a protoboard Adafruit "Proto Shield for Arduino" (PRODUCT ID: 2077).

The PCA10040 board follows the Arduino shield form-factor, so the protoboard plugs into the PCA10040.

# Wiring
The accelerometer board is wired to the PCA10040 board though the prototype board.
The wiring is as follows:
* Device SCL to protoboard SCL
* Device SDA to protoboard SDA
* Device CS to protoboard Vdd (note: selects for I2C I/F operations)
* Device 3V0 to protoboard Vdd
* Device GND to protoboard Gnd
* Device INT to protoboard pin 1 (analog in)


# Configuration
* BUS[0|1] selector for I2C bus controller
* Pin:  SCL pin -- PCA10040's P0.27 coresponds to Arduino SCL shield pin
* Pin:  SDA pin -- PCA10040's P0.26 coresponds to Arduino SDA shield pin
* addr: Slave address -- (0x30 >> 1) == 0x18 == 24 (default)
* irq:  IRQ pin -- default is PCA10040's P0.03 pin
