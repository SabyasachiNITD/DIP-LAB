#Day -2 
#Assignment 1
#Addition of two images 

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread("1st.jpg",0)
img2=cv2.imread("2nd.jpg",0)

img=img1+img2

fig=plt.figure()
ax1= fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

ax1.imshow(img1,cmap="gray",interpolation=None)
ax2.imshow(img2,cmap="gray",interpolation=None)
ax3.imshow(img,cmap="gray",interpolation=None)


ax1.axis("off")
ax2.axis("off")
ax3.axis("off")

plt.show()

#print(type(img1))

# print("max of added image:" np.amax(img))
# print("min of added image:" np.amin(img))



