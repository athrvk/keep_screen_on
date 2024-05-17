from win32gui import SendMessageTimeout
from win32api import mouse_event
from win32con import HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MOUSEEVENTF_MOVE

class Screen:
    __HWND_BROADCAST = HWND_BROADCAST
    __WM_SYSCOMMAND = WM_SYSCOMMAND
    __SC_MONITORPOWER = SC_MONITORPOWER
    __MONITOROFF = 2
    __MOUSEEVENTF_MOVE = MOUSEEVENTF_MOVE


    # to turn off using win32 module:-
    @property
    def turnOff(self):
        SendMessageTimeout(self.__HWND_BROADCAST, self.__WM_SYSCOMMAND, self.__SC_MONITORPOWER, self.__MONITOROFF, 0x0002, 1000)

    
    #to turn on by moving mouse by 1px :-
    @property
    def turnOn(self):
        # print(win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1))
        mouse_event(self.__MOUSEEVENTF_MOVE, 0, 1, 0, 0)
