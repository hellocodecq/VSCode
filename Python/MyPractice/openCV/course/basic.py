import cv2 as cv
from cv2 import dilate
from numpy import diag


img = cv.imread(r'C:\Users\KMJ514\Desktop\VSCode\Python\course\openCV\src\zjl.png')
cv.imshow('img',img)

# 1. converting to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. resize
# resized = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow("resized",resized)

# 3. cropping : 截取
# cropped = resized[150:300,100:300]
# cv.imshow("cropped",cropped)

# flipping, -1, 0, 1; h%v, v, h
flip = cv.flip(img, 0)

# blur                      (1,1)~(9,9)
# blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# Edge Cascade
canny = cv.Canny(img, 125,175)
cv.imshow('canny', canny)

# Dilating the img          ?       thickness of border
dilated = cv.dilate(img, (3,3), iterations=1)
cv.imshow('dilated',dilated)

# Eroding
eroded = cv.erode(img, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# cv.imshow("grey",grey)
cv.waitKey(0)