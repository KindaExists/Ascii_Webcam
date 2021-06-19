import cv2

cv2.namedWindow("test")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    frame = cv2.resize(frame, (160, 120))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("preview", gray)

    if cv2.waitKey(20) == 27:
        break

vc.release()
cv2.destroyWindow("test")