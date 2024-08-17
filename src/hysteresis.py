class HysteresisController:
    def __init__(self, relay, target_value, deviation=None, deviation_upper=None, deviation_lower=None):
        """
        Initializes the HysteresisController.

        Args:
            relay (object): An object with `turn_on()`, `turn_off()` and `get_state()` methods to control the relay.
            target_value (float): The desired value for the process variable.
            deviation (float, optional): A single deviation value to be used for both upper and lower deviations.
                Defaults to None.
            deviation_upper (float, optional): The allowable positive deviation from the target value before switching
                the relay off. Defaults to None.
            deviation_lower (float, optional): The allowable negative deviation from the target value before switching
                the relay on. Defaults to None.

        Raises:
            ValueError: If neither a single deviation nor both deviation_upper and deviation_lower are provided.
        """
        self.relay = relay
        self.target_temperature = target_value

        # Guard clause to ensure either deviation or both deviation_upper and deviation_lower are provided
        if deviation is None and (deviation_upper is None or deviation_lower is None):
            raise ValueError("Either provide a single deviation, or both deviation_upper and deviation_lower.")

        if deviation is not None:
            # If a single deviation is provided, use it for both upper and lower deviations
            self.deviation_upper = deviation
            self.deviation_lower = deviation
        else:
            # If individual deviations are provided, use them
            self.deviation_upper = deviation_upper
            self.deviation_lower = deviation_lower

    def control(self, temperature):
        """
        Executes one control loop iteration based on the given temperature.

        Args:
            temperature (float): The current temperature to be used for control logic.

        Returns:
            float: The input temperature value.
        """
        if temperature < (self.target_temperature - self.deviation_lower):
            if self.relay.get_state() is False:
                print("Turning relay ON\n")
                self.relay.turn_on()
        elif temperature > (self.target_temperature + self.deviation_upper):
            if self.relay.get_state() is True:
                print("Turning relay OFF\n")
                self.relay.turn_off()

        return temperature
