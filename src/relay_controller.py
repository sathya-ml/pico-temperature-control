from machine import Pin


class RelayController:
    """
    A class to control a relay connected to a Raspberry Pi Pico.

    Attributes:
        pin (Pin): The Pin object used to control the relay.
        active_low (bool): Flag indicating if the relay is activated by a LOW signal.
    """

    def __init__(self, pin_num, active_low=False):
        """
        Initializes the RelayController with the specified pin number and activation mode.

        Args:
            pin_num (int): The GPIO pin number connected to the relay control signal.
            active_low (bool, optional): If True, the relay is activated by a LOW signal;
                                          if False, by a HIGH signal. Defaults to False.
        """
        self.pin = Pin(pin_num, Pin.OUT)
        self.active_low = active_low
        self.set_state(False)  # Initially turn off the relay (common behavior)

    def set_state(self, state):
        """
        Sets the state of the relay.

        Args:
            state (bool): If True, turns on the relay; if False, turns it off.

        Returns:
            None
        """
        if self.active_low:
            self.pin.value(0 if state else 1)  # Set pin value based on activation mode
        else:
            self.pin.value(1 if state else 0)

    def turn_on(self):
        """
        Turns on the relay.

        Returns:
            None
        """
        self.set_state(True)

    def turn_off(self):
        """
        Turns off the relay.

        Returns:
            None
        """
        self.set_state(False)

    def toggle(self):
        """
        Toggles the state of the relay.

        Returns:
            None
        """
        self.set_state(not self.get_state())

    def get_state(self):
        """
        Retrieves the current state of the relay.

        Returns:
            bool: True if the relay is on, False if off.
        """
        return self.pin.value() != self.active_low
