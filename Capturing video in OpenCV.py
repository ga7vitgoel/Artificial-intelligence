import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()

    #Display the resulting frame
    cv.imshow('frame',frame)
    key = cv.waitKey(10)
    if key == 27: #wait for ESC key to exit
        break
    
#When everything done, release the capture
cam.release()
cv.destroyAllWindows()
