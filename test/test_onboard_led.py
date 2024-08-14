from time import sleep

import const
from led_controller import LEDController

onboard_led = LEDController(const.ONBOARD_LED_PIN_NUM)

onboard_led.turn_on()
sleep(3)
onboard_led.turn_off()
