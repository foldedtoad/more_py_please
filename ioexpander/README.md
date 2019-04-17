
# IOExpander for Nordic nRF52 Eval Boards -- PCA10040 and PCA10056

This MicroPython module is for the Nordic nRF52 Eval Boards specifically. 
The PCA10040, PCA10056 and the PCA10028 (nRF51) all use the PCAL6408A IOExpander chip.
While the PCA10040 and PCA10056 assign pin P0.17 as the interrupt pin, the PCA10028 assigns interrupts to pin P0.21.

The goal of this module is pedagogical in nature, e.g. to give the basics for this ioexpander's operation.

On the PCA10040 or PCA10056 board, you will need to defeat the default Button and LED configuration.  
The simplest and surest way is to jumper the `SHIELD_DETECT` pin on the J5 header (ICSP) to a `GND` pin (see the PCA10040 schematic for details). This was necessary because the pins on J5 of the PCA10040 board were too long and didn't match many of the arduino shield boards. The J5 pins were also trimmed (clipped) a bit to keep them from shorting on some arduino shield boards.  

By shorting SHIELD_DETECT to ground, the PCAL6408A be provided power and become active.
In addition, the GPIO pins (by default assigned for Button/LED support) will be freed for general use.  

The ./nrf/boards/pca10040/mpconfigboard.h file needs the following configuration change to remove the default Button/LED support.

```
#define MICROPY_HW_HAS_LED          (0)  // set to 0 if using ioexpander
```
Of course, you will need to rebuild MicroPython to pick-up this config change.

## Testing Output
The console output will look like this --
```
start ioexpander
Switches: press buttons
Switch 3 pressed
         released
Switch 3 pressed
         released
Switch 1 pressed
         released
Switch 2 pressed
         released
Switch 4 pressed
         released
Switch 3 pressed
         released
stop  ioexpander
>>> 
```

