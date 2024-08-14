from time import sleep

import const
from dht22_controller import DHT22SensorController

dht22 = DHT22SensorController(const.DHT22_PIN_NUM)
NUM_READINGS = 20

for _ in range(NUM_READINGS):
    temperature, humidity = dht22.read()
    sleep(const.DHT22_SAMPLING_INTERVAL)

    print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
