from time import sleep

import const
from led_controller import LEDController

attached_led = LEDController(const.ATTACHED_LED_PIN_NUM)

attached_led.turn_on()
sleep(3)
attached_led.turn_off()
