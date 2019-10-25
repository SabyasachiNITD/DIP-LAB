import cv2
import maplotlib.pyplot as plt 
import numpy as np 

img =cv2.imread("2nd.tif",0)

width = int(img.shape[1])
height = int(img.shape[0])




x = int(input("Enter the times to multiply:"))



for i in range(height):
	for i in range(width):
		img[i][j] =((img[i][j]//32) + 15)
