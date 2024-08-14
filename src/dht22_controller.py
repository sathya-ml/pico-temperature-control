import dht
from machine import Pin


class SensorReadingError(Exception):
    """
    Exception raised for errors encountered during the sensor reading process.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message="Failed to read sensor data"):
        """
        Initializes the SensorReadingError with an optional custom message.

        Args:
            message (str, optional): A descriptive message explaining the error. Defaults to
                "Failed to read sensor data".
        """
        self.message = message
        super().__init__(self.message)


class DHT22SensorController:
    def __init__(self, pin_num):
        """
        Initializes the DHT22SensorController with the specified pin number.

        Args:
            pin_num (int): The GPIO pin number to which the DHT22 sensor is connected.
        """
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.sensor = dht.DHT22(self.pin)

    def read(self):
        """
        Reads the temperature and humidity from the DHT22 sensor.

        Returns:
            tuple: A tuple containing the temperature (in Celsius) and humidity (as a percentage).

        Raises:
            SensorReadingError: If there is an OSError during the sensor read operation.
        """
        try:
            self.sensor.measure()
            return self.sensor.temperature(), self.sensor.humidity()
        except OSError:
            print("Failed to read sensor.")
            raise SensorReadingError()
