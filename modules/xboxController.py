import pygame, sys
from threading import Thread
from time import sleep

class XboxController:

    def __init__(self):

        pygame.init()
        joystick_count = pygame.joystick.get_count()
        
        if joystick_count == 0:
            # if no joysticks, quit program safely
            raise Exception("Error. No joysticks found!")
        else:
            # initialise joystick
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        t = Thread(target=self.updateLoop, daemon=True)
        t.start()

    def updateLoop(self):
        while(True):
            for event in pygame.event.get():
                # loop through events, if window shut down, quit program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            sleep(.01)

    def getAxis(self, number):
        return self.joystick.get_axis(number)
 
    def getButton(self, number):
        # returns 1 or 0 - pressed or not
        return self.joystick.get_button(number)

    def getHat(self, number):
        # returns tuple with values either 1, 0 or -1
        return self.joystick.get_hat(number)

    def getInfo(self):
        return self.joystick.get_numaxes()
