import cv2 as cv
import numpy as np

#create a black image
img = np.zeros((512,512,3),np.uint8)

# Draw a diagonal blue line with the thickness of 5px by giving 2 end points
cv.line(img,(0,0),(511,511),(255,0,0),5)

#draw a green rectangle with thickness of 3px by giving two opposite corners
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Draw a red solid circle with thickness of 3px by giving center and radius
cv.circle(img,(447,63),63,(0,0,255),-1)

#draw a yellow polygon by giving vertices
pts = np.array([[100,50],[200,300],[70,200],[50,100]],np.int32)
cv.polylines(img,[pts],True,(0,255,255),3)

#write text by giving bottom left corner,font type, size, color and thickness
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'skyfi Labs',(0,480),font,2,(255,255,255),2)


cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyALLWindows()
