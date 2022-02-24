import cv2 as cv
# import matplotlib as plt


# color spaces 颜色空间

img = cv.imread(r'C:\Users\KMJ514\Desktop\VSCode\Python\course\openCV\src\zjl.png')
cv.imshow("img",img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rbg', rgb)


cv.waitKey(0)