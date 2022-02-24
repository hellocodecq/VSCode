import cv2 as cv
import numpy as np

"""确定边缘, 传入图片时, 使用灰度图"""

## 方法一  模糊化
def blur_method(img):
    blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
    cv.imshow("blur", blur)

    # 边缘
    canny = cv.Canny(blur,125,127)
    cv.imshow('canny', canny)

    # contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    # print(len(contours))

## 方法2
def tresh_method(img):
    blank = np.zeros(img.shape, dtype='uint8')
    ret, thresh = cv.threshold(img,124, 255, cv.THRESH_BINARY)
    cv.imshow("thresh",thresh)
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    #                               all contours   pen color pensize
    print('len contours：',len(contours))
    cv.drawContours(blank, contours,    -1,        (0,0,255),  1)
    cv.imshow('contours drawn', blank)
    cv.waitKey(0)

if __name__ == '__main__':
    imgs = cv.imread(r'C:\Users\KMJ514\Desktop\VSCode\Python\MyPractice\openCV\src\Mario.jfif')
    grey = cv.cvtColor(imgs,cv.COLOR_BGR2GRAY)
    cv.imshow('grey', grey)


    blur_method(grey)
    tresh_method(grey)
    cv.waitKey(0)