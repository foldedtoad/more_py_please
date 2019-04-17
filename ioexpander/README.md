
# IOExpander for Nordic nRF52 Eval Boards -- PCA10040 and PCA10056

This MicroPython module is for the Nordic nRF52 Eval Boards specifically.  
If you have another board which happens to have the PCAL series ioexpander, the this code may be useful as well.  
The goal of this code is to give a basic outline of this ioexpanders support requirements.

On the PCA10040 or PCA10056 board, you will need to defeat the default Button and LED configuration.  
The simplest and surest way is to jumper the `SHIELD_DETECT` pin on the J5 header (ICSP) to a `GND` pin (see the PCA10040 schematic for details). This was necessary because the pins on J5 of the PCA10040 board were too long and didn't match many of the arduino shield boards. The J5 pins were also trimmed (clipped) a bit to keep them from shorting on some arduino shield boards.  

In doing the above wiring, the GPIO pins (by default assigned for Button/LED support) will be freed for general use.  

The ./nrf/boards/pca10040/mpconfigboard.h file needs the following configuration change to remove the default Button/LED support.

```
#define MICROPY_HW_HAS_LED          (0)  // set to 0 if using ioexpander
```
