import pyglet
from time import sleep


joysticks = pyglet.input.get_joysticks()

joystick = joysticks[0]
joystick.open()

while(not joystick.buttons[0]):
    sleep(.1)
