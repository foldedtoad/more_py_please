# more_py_please
This is my collection of MicroPython projects.  
Since I have worked extensibly with Nordic and their products, e.g. I have a lot of their eval boards, most of the code has been developed on Nordic's PCA10040 (nRF52832) and PCA10056 (nRF82840) boards.

I like these boards because Nordic's boards have on-board Segger JLink support.  
This is very handy when coding in a coffee shop venue, as I often do: just a small discrete eval board connected to my laptop via one USB cable.

In general, most of the code was developed without depending on the SoftDevice support. As far as I know, there is nothing to prevent the inclusion of the SoftDevice if you have some BLE-requirement.  Excluding the SoftDevice frees a fair amount of flash memory.

Most of the code is purposefully kept simple (KISS method) to illustrate some basic technology or technique.
Its assumed that these building-blocks could be stitched together into a more complex application.

## USART Issues
The UART support for the nRF52 port appears to have some flowcontrol problems. When using REPL-base access (direct or BLE-based) it will often hang the system.  I have not investigated this in detail (yet).  During my initial investigation I found that the USB-serial adapters were presenting data to the nRF52 in 256-byte packets, but often the first packet was dropped. See the Ellisys USB trace data below. The MicroPython stack on the nRF52 only sees Frame-6.

```
No. Time Source Destination Protocol Length Info
1 0.000000 64.24.4 host USB 288 URB_BULK out
(completed)
Frame 1: 288 bytes on wire (2304 bits), 288 bytes captured (2304 bits) on interface 0
USB URB
Leftover Capture Data: 64656620746573745f62756666657228293a0a2020202022…
0000 00 01 20 01 00 01 00 00 00 00 00 00 00 00 00 00 .. .............
0010 62 0c d4 01 00 00 00 00 00 00 40 14 02 18 04 02 b.........@.....
0020 64 65 66 20 74 65 73 74 5f 62 75 66 66 65 72 28 def test_buffer(
0030 29 3a 0a 20 20 20 20 22 22 22 43 68 65 63 6b 73 ):. """Checks
0040 20 74 68 65 20 6d 69 63 72 6f 70 79 74 68 6f 6e the micropython
0050 20 66 69 72 6d 77 61 72 65 20 74 6f 20 73 65 65 firmware to see
0060 20 69 66 20 73 79 73 2e 73 74 64 69 6e 2e 62 75 if sys.stdin.bu
0070 66 66 65 72 20 65 78 69 73 74 73 2e 22 22 22 0a ffer exists.""".
0080 20 20 20 20 69 6d 70 6f 72 74 20 73 79 73 0a 20 import sys.
0090 20 20 20 74 72 79 3a 0a 20 20 20 20 20 20 20 20 try:.
00a0 5f 20 3d 20 73 79 73 2e 73 74 64 69 6e 2e 62 75 _ = sys.stdin.bu
00b0 66 66 65 72 0a 20 20 20 20 20 20 20 20 72 65 74 ffer. ret
00c0 75 72 6e 20 54 72 75 65 0a 20 20 20 20 65 78 63 urn True. exc
00d0 65 70 74 3a 0a 20 20 20 20 20 20 20 20 72 65 74 ept:. ret
00e0 75 72 6e 20 46 61 6c 73 65 0a 6f 75 74 70 75 74 urn False.output
00f0 20 3d 20 74 65 73 74 5f 62 75 66 66 65 72 28 29 = test_buffer()
0100 0a 69 66 20 6f 75 74 70 75 74 20 69 73 20 4e 6f .if output is No
0110 6e 65 3a 0a 20 20 20 70 72 69 6e 74 28 22 4e 6f ne:. print("No

No. Time Source Destination Protocol Length Info
2 0.009307 64.24.7 host USB 32 URB_INTERRUPT in
(submitted)
Frame 2: 32 bytes on wire (256 bits), 32 bytes captured (256 bits) on interface 0
USB URB
0000 00 01 20 00 08 00 00 00 00 50 00 e0 00 00 00 00 .. ......P......
0010 64 0c d4 01 00 00 00 00 00 00 40 14 02 18 87 03 d.........@.....

No. Time Source Destination Protocol Length Info
3 0.010050 80.63.1 host USB 40 URB_INTERRUPT in
(completed)
Frame 3: 40 bytes on wire (320 bits), 40 bytes captured (320 bits) on interface 0
USB URB
Leftover Capture Data: 0000000000000000
0000 00 01 20 01 08 00 00 00 00 00 00 00 00 00 00 00 .. .............
0010 4d 0c d4 01 00 00 00 00 00 00 50 14 01 3f 81 03 M.........P..?..
0020 00 00 00 00 00 00 00 00 ........

No. Time Source Destination Protocol Length Info
4 0.010125 80.63.1 host USB 32 URB_INTERRUPT in
(submitted)
Frame 4: 32 bytes on wire (256 bits), 32 bytes captured (256 bits) on interface 0
USB URB
0000 00 01 20 00 08 00 00 00 00 00 00 00 00 00 00 00 .. .............
0010 65 0c d4 01 00 00 00 00 00 00 50 14 01 3f 81 03 e.........P..?..

No. Time Source Destination Protocol Length Info
5 0.014606 64.24.4 host USB 32 URB_BULK out
(submitted)
Frame 5: 32 bytes on wire (256 bits), 32 bytes captured (256 bits) on interface 0
USB URB
0000 00 01 20 00 1c 00 00 00 00 00 00 00 00 00 00 00 .. .............
0010 67 0c d4 01 00 00 00 00 00 00 40 14 02 18 04 02 g.........@.....

No. Time Source Destination Protocol Length Info
6 0.014694 64.24.4 host USB 60 URB_BULK out
(completed)
Frame 6: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
USB URB
Leftover Capture Data: 6e6522290a656c73653a0a2020207072696e74286f757470…
0000 00 01 20 01 1c 00 00 00 00 00 00 00 00 00 00 00 .. .............
0010 67 0c d4 01 00 00 00 00 00 00 40 14 02 18 04 02 g.........@.....
0020 6e 65 22 29 0a 65 6c 73 65 3a 0a 20 20 20 70 72 ne").else:. pr
0030 69 6e 74 28 6f 75 74 70 75 74 29 0a             int(output).
```

