import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread("2nd.tif",0)

img2= img & 15
img1 = (img>>4)


img1 = cv2.equalizeHist(img1)

cv2.imshow("1",img2)
cv2.imshow("2",img1)
cv2.imshow("3",img)

cv2.waitKey(0)

# fig=plt.figure()
# ax1= fig.add_subplot(1,3,1)
# ax2 = fig.add_subplot(1,3,3)
# ax3=fig.add_subplot(1,3,2)

# ax1.imshow(img,cmap="gray",interpolation=None)
# ax2.imshow(img2,cmap="gray",interpolation=None)
# ax3.imshow(img1,cmap="gray",interpolation=None)

# ax1.axis("off")
# ax2.axis("off")

# plt.show()

