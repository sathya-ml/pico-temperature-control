class LedTemperatureSignal:
    def __init__(self, attached_led, target_temperature, max_tolerance, blinking_interval=250):
        """
        Initializes the LedTemperatureSignal.

        Args:
            attached_led (object): An object with `turn_on()`, `start_blinking()`, and `turn_off()` methods to control the LED.
            target_temperature (float): The desired temperature that the system aims to maintain.
            max_tolerance (float): The maximum allowable deviation from the target temperature before changing the LED signal.
            blinking_interval (int, optional): The interval in milliseconds for blinking when the temperature exceeds the maximum bound. Defaults to 250.
        """
        self.attached_led = attached_led
        self.target_temperature = target_temperature
        self.max_tolerance = max_tolerance
        self.blinking_interval = blinking_interval

        self.temperature_min_bound = self.target_temperature - self.max_tolerance
        self.temperature_max_bound = self.target_temperature + self.max_tolerance

    def signal(self, temperature):
        """
        Adjusts the LED signal based on the current temperature.

        Args:
            temperature (float): The current temperature to be used for controlling the LED.

        Returns:
            None: This method does not return any value.
        """
        if temperature < self.temperature_min_bound:
            self.attached_led.turn_on()
        elif temperature > self.temperature_max_bound:
            self.attached_led.start_blinking(interval_ms=self.blinking_interval)
        else:
            self.attached_led.turn_off()
