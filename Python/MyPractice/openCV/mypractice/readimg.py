import cv2 as cv
from mycv import *



if __name__ == "__main__":
    img = cv.imread(r"C:\Users\KMJ514\Desktop\VSCode\Python\course\openCV\src\drem.jpg")
    cv.imshow("flip image", flip_image(img))

    cv.waitKey(0)