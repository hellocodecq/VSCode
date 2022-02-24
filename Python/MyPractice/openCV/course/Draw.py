import cv2 as cv
import numpy as np

absolute_path = r"C:\Users\KMJ514\Desktop\VSCode\Python\openCV\src\Mario.jpg"


# 1. create a blank picture
# size:500x500, channels:3(BGR)
# uint8 means a picture
blank = np.zeros((500,500,3),dtype="uint8")

# 2. change color of the picture, draw a rectangle
# height from 0 to 100, width from 100 to 200,
# change this area to green
#       h       w
blank[0:100, 100:200] = 0,255,0


# 3. create a rectangle
#           img     start   end     color   thickness, // linetype
cv.rectangle(blank,(0,0),(100,100),(0,0,255),2)
# this code above create a empty rectangle with color:red, thickness:2

# 4. create a solid rectangle
cv.rectangle(blank, (0,250),(300,300),(255,0,0),-1)

# 5. create a circle
#           img   center  radius    color  thickness
cv.circle(blank, (43,250),   40 ,(0,255,0), 3)

# 6. create a solid circle
cv.circle(blank, (183,303),   40 ,(0,255,0), -1)

# 7. draw a line
#              start    end         color       thickness
cv.line(blank, (0,0),  (250,250),(255,255,255), 3)

# 8. write a text
cv.putText(blank,"HelloCode",(200,400),cv.FONT_HERSHEY_TRIPLEX,1.1,(255,255,255),2)

cv.imshow('Blank',blank)
cv.waitKey(0)


