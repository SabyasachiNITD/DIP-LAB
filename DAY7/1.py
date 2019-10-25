import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# def sliding_window(image, stepSize, windowSize):
# 	# slide a window across the image
# 	for y in range(0, image.shape[0], stepSize):
# 		for x in range(0, image.shape[1], stepSize):
# 			# yield the current window
# 			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])



img = cv2.imread('man.jpeg',0)

# rows,cols = 


kernel = np.ones((3,3),np.uint8)

img_e = cv2.erode(img,kernel,iterations=1)
dialation = cv2.dilate(img,kernel,iterations=1)
img_o = cv2.morphologyEx(img_e,cv2.MORPH_OPEN,kernel)
img_d = cv2.dilate(img_o,kernel,iterations=1)

closing=cv2.morphologyEx(img_o,cv2.MORPH_CLOSE,kernel)

cv2.imshow('input',img)
cv2.imshow('eroded(a)',img_e)
cv2.imshow('opening(b)',img_o)
cv2.imshow('dialation(c)',img_d)
cv2.imshow('closing(d)',closing)
cv2.imshow('boundary (2)',dialation-img_e)
cv2.waitKey(0)

