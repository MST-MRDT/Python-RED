from modules import xboxController
from time import sleep
import pygame

myController = xboxController.XboxController()

while True:

    print()
    print("************")
    print()

    print("Left Joystick X: ", myController.getAxis(0))
    print("Left Joystick Y: ", myController.getAxis(1))

    print("Right Joystick X: ", myController.getAxis(3))
    print("Right Joystick Y: ", myController.getAxis(4))
    
    print("Left Trigger: ", myController.getAxis(2))
    #print("Right Trigger: ", myController.getAxis(5))
    
    print(myController.getButton(0))
    
    print(myController.getHat(0))

    sleep(0.15)
