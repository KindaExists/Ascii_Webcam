
"""
Notable Issues to fix later
    1) Program cannot handle terminal resizing, this is most likely a problem due to this running in Windows

"""

import cv2
import curses


def main(stdscr):
    cv2.namedWindow("test")
    vc = cv2.VideoCapture(0)

    w, h = 120, 90  # 160, 120
    pad_multiplier = 5
    pad = curses.newpad(2000, 2000)


    gscale = " .:-=+*#%@"
    # 10 Levels of grayscale

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
        print("Webcam is Turned off")

    while rval:
        pad.clear()
        s_h, s_w = stdscr.getmaxyx()

        rval, frame = vc.read()
        cv2.imshow("test", frame)

        frame = cv2.resize(frame, (w, h))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ascii_vals = [[gscale[round(gray[y, x] * (9/256))] for x in range(w)] for y in range(h)]
        [pad.addstr(y, 0, '  '.join(ascii_vals[y])) for y in range(h)]

        pad.refresh(0, 0, 0, 0, s_h-1, s_w-1)
        if cv2.waitKey(20) == 27: # ESC key
            break
    vc.release()
    cv2.destroyWindow("test")
curses.wrapper(main)


