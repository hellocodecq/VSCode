import cv2 as cv
import mycv
import time
import os


if __name__ == "__main__":
    ba = cv.VideoCapture("./Python/openCV/src/badapple.mp4")
    delay = 0.025
    frame_list = []
    while True:
        isTrue, frame = ba.read()
        frame = mycv.resize_to_width(frame,50)
        if isTrue:
            frame_list.append(mycv.to_dot(frame))
        cv.imshow("BA",frame)
        if cv.waitKey(1) & 0xFF== ord('d'):
            break
    ba.release()
    cv.destroyAllWindows()
    time_now = time.time()
    for frame in frame_list:
        time.sleep(1/60)
        # time_now = time.time()
        os.system("cls")
        print(frame)
    
