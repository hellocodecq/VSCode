import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



if __name__ == '__main__':
    relative_path = "\src\\badapple.mp4"
    capture = cv.VideoCapture(relative_path)

    while True:
        isTrue, frame = capture.read()

        if isTrue==False:
            break
        cv.imshow("bad apple", frame)
        cv.imshow('resized', rescaleFrame(frame))

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    # relative_path = "Python\openCV\src\Mario.jpg"

    # img = cv.imread(relative_path)


    # cv.imshow("orignal",img)
    # cv.imshow("resized",rescaleFrame(img))

    # cv.waitKey(0)