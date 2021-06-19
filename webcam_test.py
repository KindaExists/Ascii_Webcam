import cv2

cv2.namedWindow("test")
vc = cv2.VideoCapture(0)

gscale = " .:-=+*#%@"
# 10 Levels of grayscale

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

w, h = 160, 120

while rval:
    rval, frame = vc.read()
    frame = cv2.resize(frame, (w, h))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("test", gray)

    thing = [[gscale[round(gray[y, x] * (9/256))] for x in range(w)] for y in range(h)]
    print('\n'.join(['  '.join(y) for y in thing]))

    if cv2.waitKey(20) == 27: # ESC key
        break

vc.release()
cv2.destroyWindow("test")