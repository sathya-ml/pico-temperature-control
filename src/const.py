# DHT22 temperature and humidity sensor
DHT22_PIN_NUM = 22  # The GPIO pin number where the sensor signal is connected to the Pico
DHT22_SAMPLING_INTERVAL = 2  # How often to read the sensor in seconds
# How many times the sensor can fail before aborting the program.
# This is to allow for some sensor failures, which sometimes happen.
# Keep in mind that the total time of malfunctioning is the product of this value and the sampling interval.
MAX_SENSOR_FAILS = 10

# LEDs
ONBOARD_LED_PIN_NUM = 25  # The onboard LED on the Raspberry Pi Pico. This should be constant, so no need to change it.
ATTACHED_LED_PIN_NUM = 13  # The GPIO pin number where the attached LED is connected to the Pico.
LED_BLINK_INTERVAL = 250  # The interval in milliseconds for blinking the LED

# Temperature control parameters
TARGET_TEMPERATURE = 25.0
# How much the temperature can deviate from the target before turning on/off the heater.
TEMPERATURE_DEVIATION_TOLERANCE = 0.5
# The maximum tolerance for the temperature before signaling the user that something's wrong.
TEMPERATURE_MAX_TOLERANCE = 2.0

# Heater relay
HEATER_RELAY_PIN_NUM = 16  # The GPIO pin number where the relay control signal is connected on the Raspberry Pi.
HEATER_RELAY_ACTIVE_LOW = False  # Whether the relay is active at low voltage or high voltage.
