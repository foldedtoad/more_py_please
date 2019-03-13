
LIS3DH accelerometer driver for Nordic nRF52 series demo boards (PCA100xx) 
Tested on Nordic PCA10040 dev board (nRF52832) with Micropython release 1.10.0

Datasheet: LIS3DH (DocID17530 Rev 2) "MEMS digital output motion sensor: ultra-low-power high-performance 3-axis "nano" accelerometer"

App Note:  AN3308 (DocID18198 Rev 3) "LIS3DH: MEMS digital output motion sensor ultra-low-power high-performance 3-axis “nano” accelerometer"

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
* Device INT to protoboard pin 1 (analog in)


Driver configuration parameters --
* BUS[0|1] selector for I2C bus controller
* Pin:  SCL pin -- PCA10040's P0.27 coresponds to Arduino SCL shield pin
* Pin:  SDA pin -- PCA10040's P0.26 coresponds to Arduino SDA shield pin
* addr: Slave address -- (0x30 >> 1) == 0x18 == 24 (default)
* irq:  IRQ pin -- default is PCA10040's P0.03 pin


--------------------------------
robin@deeplearner:~$ minicom py0

[boot] run Switch
MicroPython v1.10-152-gcff9d01-dirty on 2019-03-11; PCA10040 with NRF52832
Type "help()" for more information.
>>> 
>>> 
>>> 
paste mode; Ctrl-C to cancel, Ctrl-D to finish
=== #
=== # LIS3DH accelerometre driver for nRF5x 
=== #
=== from machine import I2C, Pin
=== import ustruct
=== import time
=== 
=== BUS0 = 0
=== BUS1 = 1
=== 
=== # Register and bitfield defs
=== #
=== REG__WHO_AM_I  = 0x0F
=== REG__CTRL_REG1 = 0x20
=== REG__CTRL_REG2 = 0x21
=== REG__CTRL_REG3 = 0x22
=== REG__CTRL_REG4 = 0x23
=== REG__CTRL_REG5 = 0x24
=== REG__CTRL_REG6 = 0x25
=== REG__OUT_X_L   = 0x28
=== REG__OUT_X_H   = 0x29
=== REG__OUT_Y_L   = 0x2A
=== REG__OUT_Y_H   = 0x2B
=== REG__OUT_Z_L   = 0x2C
=== REG__OUT_Z_H   = 0x2D
=== REG__FIFO_CTRL = 0x2E
=== REG__FIFO_SRC  = 0x2F
=== 
=== DEV_ID = 0x33
=== MULTI_READ = 0x80
=== 
=== DR_POWER_DOWN = (0<<4)
=== DR_1HZ    = (1<<4)
=== DR_10HZ   = (2<<4)
=== DR_25HZ   = (3<<4)
=== DR_50HZ   = (4<<4)
=== DR_100HZ  = (5<<4)
=== DR_200HZ  = (6<<4)
=== DR_400HZ  = (7<<4)
=== DR_1500HZ = (8<<4)
=== DR_1250HZ = (9<<4)
=== XEN = (1<<0)
=== YEN = (1<<1)
=== ZEN = (1<<2)
=== 
=== I1_TAP_EN    = (1<<7)
=== I1_INT1      = (1<<6)
=== I1_DRDY1     = (1<<4)
=== I1_WATERMARK = (1<<2)
=== I1_OVERRUN   = (1<<1)
=== 
=== BDU     = (1<<7)
=== BLE     = (1<<6)
=== FS_2G   = (0<<4)
=== FS_4G   = (1<<4)
=== FS_8G   = (2<<4)
=== FS_16G  = (3<<4)
=== HR      = (1<<3)
=== ST_NORM = (0<<1)
=== ST_0    = (1<<1)
=== ST_1    = (2<<1)
=== SIM     = (1<<0)
=== 
=== BOOT     = (1<<7)
=== FIFO_EN  = (1<<6)
=== LIR_INT1 = (1<<3)
=== D4D_INT1 = (1<<2)
=== 
=== I2_TAP_EN = (1<<7)
=== I2_INT1   = (1<<6)
=== I2_BOOT   = (1<<4)
=== I2_HL_ACT = (1<<1)
=== 
=== FM_BYPASS  = (0<<6)
=== FM_FIFO    = (1<<6)
=== FM_STREAM  = (2<<6)
=== FM_TRIGGER = (3<<6)
=== TR_INT1    = (0<<5)
=== TR_INT2    = (1<<5)
=== 
=== FF_WATERMARK = (1<<7)
=== FF_OVERRUN   = (1<<6)
=== FF_EMPTY     = (1<<5)
=== FF_FSS_MASK  = 0x1F
=== 
=== # Configuration parameters
=== #
=== SLAVE_ADDR      = 24
=== IRQ_PIN         = 3
=== WATERMARK_LEVEL = 25
=== DATA_RATE       = DR_25HZ
=== FULL_SCALE      = FS_4G
=== 
=== 
=== class LIS3DH:
=== 
===   def __init__(self, i2c, addr=24, irq=3):
===     self.i2c = i2c
===     self.addr = addr
===     self.irq = irq
=== 
===   def device_check(self):
===     who = self.i2c.readfrom_mem(self.addr, REG__WHO_AM_I, True)[0]
===     if who == DEV_ID:
===       print("found LIS3DH")
===     else:
===       print("unknown dev: 0x{:02X}".format(who))
=== 
===   def read_vector(self):
===     bytes = self.i2c.readfrom_mem(self.addr, (REG__OUT_X_L | MULTI_READ), 6)
===     sarray = ustruct.unpack('hhh', bytes)
===     vector = (sarray[0] >> 4, sarray[1] >> 4, sarray[2] >> 4)
===     return vector
=== 
===   def read_vectors_from_fifo(self):
===     fifo_count = (self.i2c.readfrom_mem(self.addr, REG__FIFO_SRC, True)[0]) & FF_FSS_MASK
===     for i in range(fifo_count):
===       vector = self.read_vector()
===       print(vector)   # NOTE: do something more interesting with this vector
===     self.fifo_toggle()
=== 
===   def device_init(self):
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG1, True)[0]
===     value = (DATA_RATE | XEN | YEN | ZEN)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG1, bytearray((value,)))
=== 
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG4, True)[0]
===     value |= (FULL_SCALE | BDU)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG4, bytearray((value,)))
=== 
===   def events_config(self):
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG6, True)[0]
===     value |= (I2_HL_ACT)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG6, bytearray((value,)))
=== 
===   def fifo_config(self):
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG3, True)[0]
===     value |= (I1_WATERMARK)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG3, bytearray((value,)))
=== 
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG4, True)[0]
===     value |= (FS_2G | BDU | HR)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG4, bytearray((value,)))
=== 
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG5, True)[0]
===     value |= (FIFO_EN)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG5, bytearray((value,)))
=== 
===     value |= (FM_FIFO | TR_INT1 | WATERMARK_LEVEL)
===     self.i2c.writeto_mem(self.addr, REG__FIFO_CTRL, bytearray((value,)))
=== 
===   def fifo_deconfig(self):
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG3, True)[0]
===     value &= ~(I1_WATERMARK)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG3, bytearray((value,)))
=== 
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG4, True)[0]
===     value &= ~(FS_2G | BDU | HR)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG4, bytearray((value,)))
=== 
===     value = self.i2c.readfrom_mem(self.addr, REG__CTRL_REG5, True)[0]
===     value &= ~(FIFO_EN)
===     self.i2c.writeto_mem(self.addr, REG__CTRL_REG5, bytearray((value,)))
=== 
===     value = (FM_BYPASS)
===     self.i2c.writeto_mem(self.addr, REG__FIFO_CTRL, bytearray((value,)))
=== 
===   def fifo_toggle(self):
===     value = (FM_BYPASS)
===     self.i2c.writeto_mem(self.addr, REG__FIFO_CTRL, bytearray((value,)))
=== 
===     value = (FM_FIFO | WATERMARK_LEVEL)
===     self.i2c.writeto_mem(self.addr, REG__FIFO_CTRL, bytearray((value,)))
=== 
===   def start(self):
===     print("start accelerometer")
===     self.device_init()
===     self.events_config()
===     self.fifo_config()
===     self.fifo_toggle()
=== 
===   def stop(self):
===     print("stop accelerometer")
===     self.fifo_deconfig()
=== 
===   def events_callback(self, pin_obj): 
===     if pin_obj.pin() == self.irq:
===       vector = self.read_vectors_from_fifo()
=== 
===   def set_events_callback(self):
===     Pin(self.irq).irq(self.events_callback, trigger=Pin.IRQ_FALLING)
=== 
=== 
=== # BUS[0|1] selector for I2C bus controller
=== # Pin:  SCL pin -- PCA10040's P0.27 coresponds to Arduino SCL shield pin
=== # Pin:  SDA pin -- PCA10040's P0.26 coresponds to Arduino SDA shield pin
=== # addr: Slave address -- (0x30 >> 1) == 0x18 == 24 (default)
=== # irq:  IRQ pin -- default is PCA10040's P0.03 pin
=== #
=== if __name__ == '__main__':
=== 
===   accel = LIS3DH( I2C(BUS1, Pin(27), Pin(26)), addr=SLAVE_ADDR, irq=IRQ_PIN )
===   accel.device_check()
===   accel.set_events_callback()
=== 
===   accel.start()
===   time.sleep_ms(20000)
===   accel.stop()
=== 
=== 
found LIS3DH
start accelerometer
(0, 0, 260)
(0, 0, 384)
(0, 4, 452)
(0, 4, 480)
(4, 4, 500)
(0, 4, 508)
(4, 4, 508)
(0, 4, 512)
(0, 4, 516)
(0, 4, 516)
(0, 8, 516)
(4, 4, 516)
// repeat //
(4, 4, 516)
(4, 4, 520)
(4, 4, 520)
(4, 4, 520)
stop accelerometer
>>> 
