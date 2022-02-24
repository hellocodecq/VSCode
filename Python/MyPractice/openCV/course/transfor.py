import cv2 as cv
import numpy as np





# 移动图片的相对位置
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions) 

# 旋转图片
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)    # default rotate point
    #                                               scale
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    demensions = (width, height)

    return cv.warpAffine(img, rotMat, demensions)


if __name__ == '__main__':
    absolute_path = r"C:\Users\KMJ514\Desktop\VSCode\Python\course\openCV\src\Mario.jpg"

    img =  cv.imread(absolute_path)


    cv.imshow("img",img)
    cv.imshow("rotated", rotate(img, -45))


    cv.waitKey(0)
