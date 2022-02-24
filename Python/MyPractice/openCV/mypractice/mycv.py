# 
# moudle: mycv.py
# description: this is a moudle of opencv (cv2 in python)

import cv2 as cv

# read images from camera, 0 is rear camera
# 1 is front camera, 2 is
def get_camera(n_camera):
    capture = cv.VideoCapture(n_camera)
    capture.set(3,480)  # 3 channels, 480pixels?
    while capture.isOpened():
        flag, img = capture.read()
        
        cv.imshow("Video", flip_image(img))
        k  = cv.waitKey(26)
        if k == ord('s'):
            cv.imwrite("test.jpg", img)
        elif k == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()

def resized(frame, dimensions):
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def resize_to_width(frame,width):
    dimen =  frame.shape[1] / width
    dimensions = (width, int(frame.shape[0]/dimen))
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def to_grey(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

def to_dot(frame):
    dot_list = ['##','$$','69','ww','hh','ii','==','--','..']
    grey = to_grey(frame)
    map = ""
    for lines in grey:
        for pixel in lines:
            num_pixels = int(pixel / 30)
            map += dot_list[num_pixels]
        map+='\n'
    return map

# flip an image, left to right, right to left
def flip_image(img):
    width = img.shape[1]
    height = img.shape[0]
    print(width, height)
    half = int(width/2)
    i = 0
    j = 0
    while(i<height):
        while(j<half):
            print("Change!",end = " ")
            img[i][j], img[i][width-j-1] = img[i][width-j-1],img[i][j]
            j+=1
        print()
        i+=1
    return img
