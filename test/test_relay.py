from time import sleep

import const
from relay_controller import RelayController

heater_relay = RelayController(
    const.HEATER_RELAY_PIN_NUM,
    active_low=const.HEATER_RELAY_ACTIVE_LOW
)

heater_relay.turn_on()
sleep(5)
heater_relay.turn_off()
