import cv2 as cv
import os

img = cv.imread("./Python/openCV/src/drem.jpg")
map = []
line = []

cv.imshow("IMG",img)

os.system("cls")
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for lines in grey:
    line = []
    for pixel in lines:
        num_pixels = int(pixel / 3)
        if num_pixels >= 80:
            line.append("..")
        elif num_pixels >= 70:
            line.append ("::")
        elif num_pixels >= 60:
            line.append("**")
        elif num_pixels >= 50:
            line.append("==")
        elif num_pixels >= 40:
            line.append("ww")
        elif num_pixels >= 30:
            line.append("96")
        elif num_pixels >= 20:
            line.append("$$")
        elif num_pixels >= 10:
            line.append("@@")
        else:
            line.append("##")

    map.append(line)
for lines in map:
    for item in lines:
        print(item, end="")
    print()

cv.waitKey()