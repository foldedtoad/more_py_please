#
# IO-Expender (PCAL6408A) driver for nRF5x (PCA10028, PCA10040, PCA10056 boards)
# See PCAL6408A datasheet for programming details
#
from machine import I2C, Pin
import time

BUS0 = 0
BUS1 = 1

# Configuration parameters
#
SLAVE_ADDR      = 32
IRQ_PIN         = 17

INPUT                       = 0x00
OUTPUT                      = 0x01
POLARITY_INVERSION          = 0x02 
CONFIGURATION               = 0x03
OUTPUT_DRIVE_STRENGTH_0     = 0x40
OUTPUT_DRIVE_STRENGTH_1     = 0x41
INPUT_LATCH                 = 0x42
PULL_UP_DOWN_ENABLE         = 0x43
PULL_UP_DOWN_SELECTION      = 0x44
INTERRUPT_MASK              = 0x45
INTERRUPT_STATUS            = 0x46
OUTPUT_PORT_CONFIGURATION   = 0x4F 

class PCAL6408A:

  def __init__(self, i2c, addr=32, irq=17):
    self.i2c = i2c
    self.addr = addr
    self.irq = irq

  def start(self):
    print("start ioexpander")

    # Do configuration: # pins[0-3] input, pins[4-7] input
    value = 0xF0
    self.i2c.writeto_mem(self.addr, CONFIGURATION, bytearray((value,)))

    value = 0x0F     # note: logic inversion
    self.i2c.writeto_mem(self.addr, INTERRUPT_MASK, bytearray((value,)))

  def stop(self):
    print("stop ioexpander")

    # Do reset:  set regs back to POR value
    value = 0xFF 
    self.i2c.writeto_mem(self.addr, INTERRUPT_MASK, bytearray((value,)))

    value = 0xFF
    self.i2c.writeto_mem(self.addr, CONFIGURATION, bytearray((value,)))

  def events_callback(self, pin_obj): 
    if (pin_obj.pin() == self.irq):
      print("ioexp: irq")

  def set_events_callback(self):
    Pin(self.irq).irq(self.events_callback, trigger=Pin.IRQ_FALLING)


# BUS[0|1] selector for I2C bus controller
# Pin:  SCL pin -- PCA10040's P0.27 coresponds to Arduino SCL shield pin
# Pin:  SDA pin -- PCA10040's P0.26 coresponds to Arduino SDA shield pin
# addr: Slave address -- (0x40 >> 1) == 0x20 == 32 (default)
# irq:  IRQ pin -- default is PCA10040's P0.017 pin
#d
if __name__ == '__main__':

  ioexp = PCAL6408A( I2C(BUS1, Pin(27), Pin(26)), addr=SLAVE_ADDR, irq=IRQ_PIN )

  ioexp.start()
  time.sleep_ms(10000)
  ioexp.stop()
