import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread("2nd.tif",0)

img1 = (img>>4)

fig=plt.figure()
ax1= fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

ax1.imshow(img,cmap="gray",interpolation=None)
ax2.imshow(img1,cmap="gray",interpolation=None)

ax1.axis("off")
ax2.axis("off")

plt.show()

