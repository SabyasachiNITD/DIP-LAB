import cv2
import numpy as np
import random 
import matplotlib.pyplot as plt


def gaussian(image):
	row,col= image.shape
	mean = 0
	var = 300
	sigma = var**0.5
	gauss = np.random.normal(mean,sigma,(row,col))
	gauss = gauss.reshape(row,col)
	noisy = image + gauss
	return noisy

image = cv2.imread("1.tif",0)
noise_image = gaussian(image)

plt.subplot(121),plt.imshow(image,cmap="gray")
plt.title("Image"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(noise_image,cmap="gray")
plt.title("gaussian_noisy_image"),plt.xticks([]),plt.yticks([])
plt.show()

plt.hist(noise_image[100:200,100:200].ravel(),255,[0,255])
plt.show()
