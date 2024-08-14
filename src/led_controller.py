from machine import Pin, Timer


class LEDController:
    """
    A class to control the onboard LED on a Raspberry Pi Pico,
    including non-blocking blinking functionality.

    Attributes:
        pin (Pin): The Pin object controlling the LED.
        timer (Timer or None): Timer object used for blinking; initialized later.
        blinking (bool): Flag indicating whether blinking is active.
    """

    def __init__(self, pin_num):
        """
        Initializes the LEDController with the given pin number.

        Args:
            pin_num (int): The GPIO pin number connected to the onboard LED.
        """
        self.pin = Pin(pin_num, Pin.OUT)
        self.pin.value(0)  # Initially turn off the LED (active-low)
        self.timer = None  # Timer object for blinking (initialized later)
        self.blinking = False  # Flag to control blinking state

    def turn_on(self):
        """
        Turns on the onboard LED and stops any ongoing blinking.

        Returns:
            None
        """
        self.pin.value(1)
        self.stop_blinking()  # Stop blinking if previously enabled

    def turn_off(self):
        """
        Turns off the onboard LED and stops any ongoing blinking.

        Returns:
            None
        """
        self.pin.value(0)
        self.stop_blinking()  # Stop blinking if previously enabled

    def toggle(self):
        """
        Toggles the state of the onboard LED (on becomes off, off becomes on)
        and stops any ongoing blinking.

        Returns:
            None
        """
        self.pin.value(not self.pin.value())
        self.stop_blinking()  # Stop blinking if previously enabled

    def start_blinking(self, interval_ms):
        """
        Starts blinking the LED with a specified interval in milliseconds.

        Args:
            interval_ms (int): The interval between LED state changes in milliseconds.

        Returns:
            None
        """
        if self.timer is None:
            self.timer = Timer()
        self.blinking = True
        self.timer.init(period=interval_ms, mode=Timer.PERIODIC, callback=self._blink_handler)

    def stop_blinking(self):
        """
        Stops the LED from blinking.

        Returns:
            None
        """
        if self.timer is not None:
            self.blinking = False
            self.timer.deinit()

    def _blink_handler(self, tim):
        """
        Internal interrupt handler that toggles the LED state. This method
        is used internally by the Timer object for periodic blinking.

        Args:
            tim (Timer): The Timer object triggering the callback.

        Returns:
            None
        """
        if self.blinking:
            self.pin.value(not self.pin.value())
