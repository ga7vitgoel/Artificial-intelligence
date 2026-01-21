import cv2 as cv
import numpy as np

img = cv.imread('hazard10.jpg')
cv.imshow('image',img)

print('The shape of the Image is ')
print(img.shape)

print('The size of the image is ')
print(img.size)

print('The datatype of the pixel values in the Image is ')
print(img.dtype)

cv.waitKey(0)
cv.destroyALLWindows()
