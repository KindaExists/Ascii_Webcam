import cv2
import curses

def main(stdscr):
    cv2.namedWindow("test")
    vc = cv2.VideoCapture(0)

    gscale = " .:-=+*#%@"
    # 10 Levels of grayscale

    w, h = 80, 60   # 160, 120


    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        stdscr.clear()

        rval, frame = vc.read()
        cv2.imshow("test", frame)

        frame = cv2.resize(frame, (w, h))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        thing = [[gscale[round(gray[y, x] * (9/256))] for x in range(w)] for y in range(h)]
        print('\n'.join(['  '.join(y) for y in thing]))

        stdscr.refresh()
        if cv2.waitKey(20) == 27: # ESC key
            break
    vc.release()
    cv2.destroyWindow("test")
curses.wrapper(main)


