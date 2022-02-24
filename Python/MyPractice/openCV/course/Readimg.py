import cv2 as cv

absolute_path = r"C:\Users\KMJ514\Desktop\VSCode\Python\openCV\src\Mario.jpg"

# read a image and show it
img = cv.imread(absolute_path)


# title, source
cv.imshow('Mario',img)


cv.waitKey(0)


