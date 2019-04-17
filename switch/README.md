# Simple Support for nRF52 PCA10040 Eval Boards Switches
This shows how to generate interrupts (aka events) in MicroPython; in this case to catch button events.  
This code does not provide debouncing logic.

The switches (buttons) activate the following functions -
* Button 1 - Display the flash directory
* Button 2 - Display filesystem stat
* Button 3 - Display uname info
* Button 4 - Do system reset
