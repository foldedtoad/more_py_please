import machine
import board
import os

#
# This switch-to-pin mapping is for the PCA10040.  Change as needed
#
SWITCH_1_PIN = 13
SWITCH_2_PIN = 14
SWITCH_3_PIN = 15
SWITCH_4_PIN = 16

LED_1 = 1
LED_2 = 2
LED_3 = 3
LED_4 = 4

RELEASED = 1
PRESSED  = 0


def switch_name(pin):
    return {
        SWITCH_1_PIN: "SWITCH_1",
        SWITCH_2_PIN: "SWITCH_2",
        SWITCH_3_PIN: "SWITCH_3",
        SWITCH_4_PIN: "SWITCH_4"
    }.get(pin, None)

def switch_state(pin):
    return {
        RELEASED: "RELEASED",
        PRESSED:  "PRESSED"
    }.get(pin, None)

def switch_to_led(pin):
    return {
        SWITCH_1_PIN: LED_1,
        SWITCH_2_PIN: LED_2,
        SWITCH_3_PIN: LED_3,
        SWITCH_4_PIN: LED_4
    }.get(pin, None)


class Switch:

    def __init__(self):
        # tbd
        return

    def switch_set_eventing(self):
        # Hook interrupts for each switch and set event callback
        machine.Pin(SWITCH_1_PIN).irq(self.switch_callback)
        machine.Pin(SWITCH_2_PIN).irq(self.switch_callback)
        machine.Pin(SWITCH_3_PIN).irq(self.switch_callback)
        machine.Pin(SWITCH_4_PIN).irq(self.switch_callback)
        return

    def switch_1_action(self):
        cwd = os.getcwd()
        print("\ndir:", cwd)
        files = os.listdir()
        for file in files:
            fields = os.stat(file)
            size = int(fields[6])
            print("%8d  %s" % (size, file))

    def switch_2_action(self):
        cwd = os.getcwd()
        fields    = os.statvfs(cwd)

        f_bsize   = int(fields[0])
        f_frsize  = int(fields[1])
        f_blocks  = int(fields[2])
        f_bfree   = int(fields[3])
        f_bavail  = int(fields[4])
        f_files   = int(fields[5])
        f_ffree   = int(fields[6])
        f_favail  = int(fields[7])
        f_flags   = int(fields[8])
        f_namemax = int(fields[9])

        print("\nFile System stat:")
        print("%-14s  %d" % ("Block-Size",   f_bsize))
        print("%-14s  %d" % ("Blocks-Total", f_blocks))
        print("%-14s  %d" % ("Blocks-Avail", f_bavail))
        print("%-14s  %d" % ("Blocks-Used",  (f_blocks - f_bavail)))
        print("%-14s  %d" % ("Bytes-Total",  (f_bsize * f_blocks)))

    def switch_3_action(self):
        print("uname:")
        print(os.uname())

    def switch_4_action(self):
        print("reset:")
        machine.reset()

    #
    # Switch callback function
    #
    def switch_callback(self, pin_obj):
        pin = pin_obj.pin()
        state = pin_obj.value()
        led = switch_to_led(pin)
        #print("event:", switch_name(pin), switch_state(state), "LED", led)

        if state == PRESSED:
            board.LED(led).on()
        elif state == RELEASED:
            board.LED(led).off()
        else:
            raise Exception("unknown LED number")

        if   pin == SWITCH_1_PIN and state == RELEASED:
            self.switch_1_action()
        elif pin == SWITCH_2_PIN and state == RELEASED:
            self.switch_2_action()
        elif pin == SWITCH_3_PIN and state == RELEASED:
            self.switch_3_action()
        elif pin == SWITCH_4_PIN and state == RELEASED:
            self.switch_4_action()

