# libraries for controlling lights
from rainbow_controller import RainbowController
from piano_lights import LightsFromPiano

controller = RainbowController(128)
piano_input = LightsFromPiano()
piano_input.run(lights_controller)