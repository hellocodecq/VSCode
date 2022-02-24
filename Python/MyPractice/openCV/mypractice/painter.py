import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype="uint8")


def OnMouse(event, x, y, flags, param):
    if event==cv.EVENT_FLAG_LBUTTON:
        blank[y,x] = (255,255,255)

cv.namedWindow('Painter')
cv.setMouseCallback('Painter',OnMouse)

while True:

    

    cv.imshow('Painter', blank)
    k = cv.waitKey(20)
    if k==ord('q'):
        break

cv.destroyAllWindows()