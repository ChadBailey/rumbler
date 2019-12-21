import sys
import cv2
import mss
import numpy
import time

from typing import NoReturn

def start() -> NoReturn:

    mon = {
        "top": 40, 
        "left": 0, 
        "width": 800, 
        "height": 640
    }

    title = "Rumbler Debug Window"
    sct = mss.mss()

    frame_delay = 0.1

    while True:
        img = numpy.asarray(sct.grab(mon))
        cv2.imshow(title, img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            sys.exit(0)

        time.sleep(frame_delay)

if __name__ == '__main__':
    start()
