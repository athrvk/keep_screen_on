from Screen import Screen
from Face import Face
from time import sleep

class KeepScreenOn:
    def __init__(self):
        self._isScreenOff = False
        self._screen = Screen()
        self._face = Face()
        self._waitTime = 10

    @property
    def isScreenOff(self):
        return self._isScreenOff

    @isScreenOff.setter
    def isScreenOff(self, state):
        self._isScreenOff = state

    @property
    def isUserLooking(self):
        return self._face.detectFace()
        

    def faceMonitor(self):
        userStatus = self.isUserLooking
        # print('faceMonitor called')
        if userStatus == -1:
            return
        # if user is looking and screen is OFF turn the screen on by moving mouse 
        elif userStatus:
            print('face detected')
            if self.isScreenOff:
                self._screen.turnOn
                self.isScreenOff = False
            # if face detected and screen is ON then wait
            else:
                sleep(30)
        # if user in not looking and screen is ON turn it OFF after waiting for 30 seconds
        elif not self.isScreenOff:
            sleep(10)
            print('screen turned off')
            self._screen.turnOff
            self.isScreenOff = True

    # redundant monitor    
    # def screenMonitor(self):
    #     print('screenMonitor called')
    #     if self.isScreenOff:
    #         if self.isUserLooking:
    #             self._screen.turnOn
    #             self.isScreenOff = False