import cv2
import numpy as np
import random 
import matplotlib.pyplot as plt


def gaussian(image):
	row,col= image.shape
	gauss = np.random.gamma(10.00,10.00,(row,col))
	noisy = image + gauss
	return noisy

image = cv2.imread("1.tif",0)
noise_image = gaussian(image)

plt.subplot(121),plt.imshow(image,cmap="gray")
plt.title("Image"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(noise_image,cmap="gray")
plt.title("gamma_noise"),plt.xticks([]),plt.yticks([])
plt.show()

plt.hist(noise_image.ravel(),255,[0,255])
plt.show()
