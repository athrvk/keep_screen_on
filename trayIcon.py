from os import path, system
from sysTrayIcon import SysTrayIcon
from keyboardEvent import Keyboard
from threading import Thread

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = system._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


class TrayIcon:
    _hoverText = "Keep Screen On"
    _mainIcon = resource_path('eye.ico')

    def __init__(self):
        SysTrayIcon(self._mainIcon, self._hoverText, self.menu_options, default_menu_index=0, window_class_name='Keep Screen On')

    
    def pauseApp(sysTrayIcon):
        Thread(target=lambda: input("Paused\n")).start()
    
    
    def resume(sysTrayIcon):
        keyboard = Keyboard()
        print('Resumed')
        Thread(target=lambda: keyboard.press()).start()
    
    menu_options = (('Pause App', None, pauseApp),
                    ('Resume', None, resume))
    