import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread("2nd.tif",0)

img1 = img - (img & 240)


img1 = cv2.equalizeHist(img1)

fig=plt.figure()
ax1= fig.add_subplot(1,2,1)
ax3=fig.add_subplot(1,2,2)

ax1.imshow(img,cmap="gray",interpolation=None)
ax3.imshow(img1,cmap="gray",interpolation=None)

ax1.axis("off")
ax3.axis("off")

plt.show()

