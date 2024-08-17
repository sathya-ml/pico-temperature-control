# Raspberry Pi Pico Temperature Controller

⚠️ Disclaimer

This project involves working with electricity, which can be dangerous and potentially life-threatening if not done
correctly.
It may include components or instructions that require working with both low-voltage circuits and higher voltages that
can be hazardous. **I am not an expert in electrical engineering or safety, and this project is provided solely for
educational and informational purposes**. If you are not experienced or qualified to handle electrical components,
particularly those involving higher voltages, please seek assistance from a professional. **The author is not
liable for any injury, damage, or loss of life resulting from following the instructions or
using the code provided in this repository. Proceed with caution and at your own risk.**

## Description

This project implements a simple temperature controller using a Raspberry Pi Pico to control a heating device based on
temperature readings from a DHT22 sensor. It's designed to maintain the temperature in a small enclosure, such as
a small greenhouse or a microgreens growing space, whose outer environment is colder than the desired
temperature inside the enclosure. It achieves this by continuously reading the temperature from a DHT22 sensor,
and controlling a relay that switches on or off an external heating device as needed.

To achieve the temperature control through a relay which can only take two states: on or off, it uses a [hysteresis
control](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control) approach similar for example to the approach used in
a storage water heater.
Given a target temperature, the heater is turned on when the temperature falls below the target minus a certain
deviation,
and turned off when the temperature rises above the target plus that same deviation.
Having such a deviation tolerance has the benefit of avoiding the relay from turning on and off too frequently,
which would case unnecessary wear on both the heating device and relay.

No assumptions are placed on the heating device and its power source, as long as it can be connected to and controlled
by a relay. It is not the most efficient or safest way to control temperature, but it is a simple and cost-effective
way.
However, there is a risk that the relay could become stuck in the on position, which could cause the heating device to
overheat and potentially cause a fire. For this reason, it is important to use a relay that is rated for the power of
the
heating device, and to monitor the enclosure's temperature to ensure it remains within safe limits.

As a safety measure, the code will blink an LED to indicate that something is wrong if the
temperature exceeds a maximum deviation, while the LED will be on if the temperature is below the target.
In case of a sensor reading failure, the code will tolerate a certain number of consecutive failures before aborting.

The code is written in MicroPython, and is designed to be readable, modular and easily extensible.
While this might somewhat impact performance, the effect is not expected to be significant given the simplicity of the
project,
and the fact that the sampling interval of the sensor is 2 seconds.
While for now it handles only temperature control, the functionality could be extended to humidity control, or to
control other components based on specific rules or sensor readings (lighting, watering, etc.).

This project was created as a personal learning exercise to explore embedded systems and working with the
Raspberry Pi Pico and MicroPython. It is not intended as a professional or production-ready solution.
Any feedback or suggestions for improvement are welcome.

## Hardware and Wiring

To build this project, you will need the following components, most of which are readily available online
or at local electronics stores:

- Raspberry Pi Pico
- DHT22 temperature and humidity sensor
- A relay module and a power source for it.
- A heating device
- LED and the corresponding resistor to limit the current.
- Breadboard and jumper wires

The wiring diagram is shown below:
![Wiring Diagram](img/circuit.svg)

The Raspberry Pi Pico must have headers soldered onto it to be able to connect it to the breadboard.
It's possible to obtain the Pico with headers pre-soldered, but if you have one without headers, you'll need to solder
them on yourself.

The reason we're using a separate power supply for the relay is that the Raspberry Pi Pico can't provide enough voltage
to trigger the relay. Most relays require 5V or higher to trigger, and the Pico can only provide 3.3V. It's also
important to connect the ground of the relay power supply to the ground of the Pico to ensure that the relay can be
triggered correctly. The relay should also be rated for the heating device you are using.

The heating device you choose, its power supply and wiring it to the relay are up to you. Make sure to follow the
correct safety procedures based on the specific device you choose.

The LED is optional and is used to indicate when something goes wrong, along with the onboard LED on the Pico.
The LED has to be connected in series with a resistor to limit the current, as the Pico's 3.3V output is likely
higher than the LED's forward voltage. Depending on the LED, the resistor value may vary.
It's up to you to calculate the correct value. There are many online calculators that can help you with this, see
for
example [this one](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-led-series-resistor).

## Installation

First, install MicroPython on your Raspberry Pi Pico. You can find instructions on how to do this on the
official Raspberry Pi website [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).

The [src/config.py](src/config.py) file contains the configuration parameters for the project.
The default values are already provided, but you should adjust them to match your specific setup:

+ the GPIO number for the DHT22 sensor
+ the GPIO number for the relay
+ the GPIO number for the LED
+ the sensor sampling interval, which for the DHT22 is 2 seconds minimum
+ the number of tolerated sensor reading fails before aborting
+ the target temperature
+ the temperature deviation - how much the measured temperature can rise or fall before the relay is triggered
+ the maximum temperature deviation - if the measured temperature exceeds the target by this value in any direction
  something is wrong, so the LED is used to indicate this to the user
+ whether the relay is active at high or low signal
+ the LED blink interval

After configuring the parameters, copy the files in [src/](src/), and the files in [test/](test/) to the Pico.
There are many ways to do this, but the
easiest is using the Thonny IDE. Instructions are available on the official Raspberry Pi website
[here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2).
The files in *test/* are optional, and are intended to test the functionality of the connected components as they are
connected to the Pico, like the relay, the LEDs, and the DHT22 sensor.
The files in *src/* contain the main code that will run on the Pico.

Once the *src/* files are on the Pico, the `main.py` script will automatically run and execute the code the next time
you power on the Pico.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
