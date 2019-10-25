import cv2
import random
import numpy as np
import matplotlib.pyplot as plt 

def sp_noise(image,prob):
	output=np.zeros(image.shape,np.uint8)
	thres = 1 - prob 
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			rdn = random.random()
			if rdn<prob:
				output[i][j]=0
			if rdn>thres:
				output[i][j]=255
			else:
				output[i][j]=image[i][j]
	return output

image = cv2.imread("1.tif",0)
noise_image = sp_noise(image,0.15)

plt.subplot(121),plt.imshow(image,cmap="gray")
plt.title("Image"),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(noise_image,cmap="gray")
plt.title("Salt_Pepper_NoiseImage"),plt.xticks([]),plt.yticks([])
plt.show()

plt.hist(noise_image[100:200,100:200].ravel(),255,[0,255])
plt.show()


