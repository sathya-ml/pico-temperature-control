from time import sleep

import const
from led_controller import LEDController
from led_signal import LedTemperatureSignaller

attached_led = LEDController(const.ATTACHED_LED_PIN_NUM)
led_temperature_signaller = LedTemperatureSignaller(
    attached_led=attached_led,
    target_temperature=const.TARGET_TEMPERATURE,
    max_tolerance=const.TEMPERATURE_MAX_TOLERANCE,
    blinking_interval=const.LED_BLINK_INTERVAL
)

led_temperature_signaller.signal(
    temperature=const.TARGET_TEMPERATURE - const.TEMPERATURE_MAX_TOLERANCE - 1
)
sleep(3)
led_temperature_signaller.signal(
    temperature=const.TARGET_TEMPERATURE + const.TEMPERATURE_MAX_TOLERANCE + 1
)
sleep(3)
led_temperature_signaller.signal(
    temperature=const.TARGET_TEMPERATURE
)
sleep(3)
