from ctypes import *
from time import sleep

class Keyboard:
        user32 = windll.user32
        kernel32 = windll.kernel32
        delay = 0.01
        enter = 0x0D

        def press(self):
                self.user32.keybd_event(self.enter, 0, 0, 0)
                sleep(self.delay)
                self.user32.keybd_event(self.enter, 0, 2, 0)
                sleep(self.delay)


