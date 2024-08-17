from time import sleep

import const
from dht22_controller import DHT22SensorController, SensorReadingError
from hysteresis import HysteresisController
from led_controller import LEDController
from led_signal import LedTemperatureSignaller
from relay_controller import RelayController


def main_loop():
    # Initialize the components
    dht22 = DHT22SensorController(const.DHT22_PIN_NUM)
    onboard_led = LEDController(const.ONBOARD_LED_PIN_NUM)
    attached_led = LEDController(const.ATTACHED_LED_PIN_NUM)
    heater_relay = RelayController(
        const.HEATER_RELAY_PIN_NUM,
        active_low=const.HEATER_RELAY_ACTIVE_LOW
    )
    hysteresis_controller = HysteresisController(
        relay=heater_relay,
        target_value=const.TARGET_TEMPERATURE,
        deviation_upper=const.TEMPERATURE_DEVIATION_TOLERANCE,
        deviation_lower=const.TEMPERATURE_DEVIATION_TOLERANCE
    )
    led_temperature_signaller = LedTemperatureSignaller(
        attached_led=attached_led,
        target_temperature=const.TARGET_TEMPERATURE,
        max_tolerance=const.TEMPERATURE_MAX_TOLERANCE,
        blinking_interval=const.LED_BLINK_INTERVAL
    )

    try:
        sensor_reading_fail_cnt = 0

        while True:
            try:
                # Read the sensor and perform control of the heater element
                temperature, _ = dht22.read()
                hysteresis_controller.control(temperature)
            except SensorReadingError:
                # Allow for the sensor to fail a few times before aborting, it sometimes happens.
                # Keep a count, if it exceeds the maximum number of fails allowed, abort.
                # Also, signal to the user that there's an issue with the sensor by turning on the onboard LED.
                onboard_led.turn_on()

                if sensor_reading_fail_cnt >= const.MAX_SENSOR_FAILS:
                    print("Temperature sensor failed - aborting")
                    break
                else:
                    sensor_reading_fail_cnt += 1
                    continue

            # We've managed to perform control, so reset the fail counter and turn off the onboard LED.
            if sensor_reading_fail_cnt > 0:
                sensor_reading_fail_cnt = 0
                onboard_led.turn_off()

            # If the temperature is too high or too low, something might have gone wrong,
            # so signal the event to the user:
            #   - If the attached LED is blinking, it's too hot.
            #   - If it's on, it's too cold.
            #   - If it's off, everything is fine.
            led_temperature_signaller.signal(temperature)

            # Sleep for a while before the next iteration
            sleep(const.DHT22_SAMPLING_INTERVAL)
    finally:
        # Turn off everything before quitting
        heater_relay.turn_off()
        onboard_led.turn_off()
        attached_led.turn_off()


if __name__ == "__main__":
    main_loop()
