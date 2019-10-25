import cv2 
import numpy as np


image = cv2.imread('man.jpeg',0)
kernel = np.ones((3,3), np.uint8) 
erosion_image = cv2.erode(image, kernel, iterations=1)
result=image-erosion_image

cv2.imshow('Input',image)
cv2.imshow('Boundary extraction',result)

cv2.waitKey(0)      
cv2.destroyAllWindows()
