from KeepScreenOn import KeepScreenOn 
from trayIcon import TrayIcon
from threading import Thread
from time import sleep, time
import traceback

def getMemoryInfo():
    from os import getpid
    from psutil import Process
    pid = getpid()
    return Process(pid).memory_info()[0]/1024**2 # memory use in MB

def runEvery(delay, task):
    next_time = time() + delay
    while True:
        
        print('memory use: ', getMemoryInfo(), 'MB')

        sleep(max(0, next_time - time()))
        try:
            task()
        except Exception:
            traceback.print_exc()
            # in production code you might want to have this instead of course:
            # logger.exception("Problem while executing repetitive task.")
        # skip tasks if we are behind schedule:
        next_time += (time() - next_time) // delay * delay + delay


def main():
    app = KeepScreenOn()
    Thread(target=lambda: TrayIcon()).start()
    Thread(target=lambda: runEvery(30, app.faceMonitor)).start()
    # threading.Thread(target=lambda: every(5, app.screenMonitor)).start()


if __name__ == "__main__":
    main()
