import gc
#import LoRaDuplexCallback
#import LoRaPingPong

#import LoRaSender
import LoRaReceiver

import config_lora
from sx127x import SX127x
from controller_nrf52 import NRF52Controller


controller = NRF52Controller()

lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss     = NRF52Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = NRF52Controller.PIN_ID_FOR_LORA_DIO0)

gc.collect()

#LoRaDuplexCallback.duplexCallback(lora)
#LoRaPingPong.ping_pong(lora)

#print("LoRaSender start")
#LoRaSender.send(lora)

print("LoRaReceiver start")
LoRaReceiver.receive(lora)
