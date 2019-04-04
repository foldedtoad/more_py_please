
def receive(lora):
    print("LoRa Receiver")

    while True:
        if lora.receivedPacket():
            try:
                payload = lora.read_payload()
                #print("*** Received message ***\n{}".format(payload.decode()))

            except Exception as e:
                print(e)

            print("Received: {} with RSSI: {}\n".format(payload.decode(), lora.packetRssi()))
