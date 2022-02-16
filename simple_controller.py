# libraries for controlling lights
import board
import neopixel
from rainbow_controller import *
from piano_lights import LightsFromPiano

controller = RainbowController(128)
piano_input = LightsFromPiano()
piano_input.run(lights_controller)