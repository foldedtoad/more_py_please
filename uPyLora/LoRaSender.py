from time import sleep_ms
#from uPySensors.ssd1306_i2c import Display

def send(lora):
    counter = 0
    print("LoRa Sender")
    #display = Display()

    while True:
        payload = 'Hello ({0})'.format(counter)
        print("Sending packet: \n{}\n".format(payload))
        print("{0} RSSI: {1}".format(payload, lora.packetRssi()))
        #display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packetRssi()))
        lora.println(payload)

        counter += 1
        sleep_ms(5 * 1000)
