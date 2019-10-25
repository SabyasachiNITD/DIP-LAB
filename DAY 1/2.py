#Day-2 
#Assignment 2
#Gray Level Manipulation 

import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("1st.jpg",0)

x=int(input("Enter x:"))

img = img//(256/x)


plt.imshow(img,cmap="gray",interpolation=None)
plt.show()