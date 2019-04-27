
def scan(lora):
    print("LoRa Scan")

    while True:

    	for x in range(6,12):

        	lora.setSpreadingFactor(x)

        	if lora.receivedPacket():
            	try:
                	payload = lora.read_payload()
            	except Exception as e:
                	print(e)

            	print("Scan: {} with RSSI: {}\n".format(payload.decode(), lora.packetRssi()))

           
