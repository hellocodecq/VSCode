import cv2 as cv


# 0: rear camera; usage: capture = cv.VideoCapture(0)
# 1: front camera;
# 2: maybe a live stream?
# string: the path of a video
video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    cv.imshow('Camera', frame)

    # waitKey(20): the frames delay 
    # and it will get an event (or a key) in the delaying time
    # onece it get a key from keyboard, it '&' with 0xFF(1111 1111)
    # so of course, it returns the key itself. that means, if I pressed
    # key 'd' in the wait time, I'll get the Ascii value of key 'd'. then
    # compare with ord('d'), the Ascii value of letter 'd', it total the 
    # same, so the sentence of 'if' get a 'True', and then, break the loop
    # why 0xFF? check this link: https://blog.csdn.net/hao5119266/article/details/104173400
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()