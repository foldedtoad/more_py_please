#import LoRaDuplexCallback
import LoRaPingPong
#import LoRaSender
#import LoRaReceiver
import config_lora
from sx127x import SX127x
from controller_nrf52 import nRF52Controller


controller = nRF52Controller()

lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss     = nRF52Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = nRF52Controller.PIN_ID_FOR_LORA_DIO0)

#LoRaDuplexCallback.duplexCallback(lora)
LoRaPingPong.ping_pong(lora)
#LoRaSender.send(lora)
#LoRaReceiver.receive(lora)
