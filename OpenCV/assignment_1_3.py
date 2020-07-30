import cv2
import numpy as np
img=cv2.imread('lena.jpg', 1)
cv2.imshow('origional', img)

img[:, :, 2] = img[:, :, 0] 
cv2.imshow('red to blue', img)
cv2.waitKey(0)
