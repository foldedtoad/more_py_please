# nRF52 Raw Radio Access 
Send and Receive raw radio packets on the MicroPython for nRF52 platform (PCA10040 and PCA10056)

These two complementary programs use the nRF52 (nRF52832 & nRF52840) hardware radio to send/receive data.
This illustrates low-level access to the radio hardware. 
Neither Bluetooth-LE or ShockBurst protocols are used and the SoftDevice is not needed or used.  

Of course, you will need two nRF52 eval boards (PCA10040 or PCA10056) to run the programs.

NOTE: The bulk of this implementation was from this [thread]( https://forum.micropython.org/viewtopic.php?t=5420) 
on the MicroPython forum.  I believe it is credited to contributor "WhiteHare".
