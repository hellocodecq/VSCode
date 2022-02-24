import cv2 as cv

path = "C:/Users/KMJ514/Desktop/VSCode/Python/openCV/src/badapple.mp4"

video = cv.VideoCapture(path)

while True:
    isTrue, frame = video.read()
    if isTrue:
        cv.imshow('Bad Apple', frame)

    if cv.waitKey(int(100/6)) & 0xFF == ord('d'):
        break