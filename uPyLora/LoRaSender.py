from time import sleep_ms

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = 'Hello ({0})'.format(counter)
        print("Sending packet: \n{}\n".format(payload))
        print("{0} RSSI: {1}".format(payload, lora.packetRssi()))
        lora.println(payload)

        counter += 1
        sleep_ms(5 * 1000)
