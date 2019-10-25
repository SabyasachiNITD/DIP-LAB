import numpy as np
import argparse
import cv2

def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k
	return output


sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")

laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
 
# construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
 
# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

kernelBank = (
	("sharpen", sharpen),
	("laplacian", laplacian),
	("sobel_x", sobelX),
	("sobel_y", sobelY)
)

image = cv2.imread("1.tif", 0)
gray = image
 
for (kernelName, kernel) in kernelBank:
	#print("[INFO] applying {} kernel".format(kernelName))
	convoleOutput = convolve(gray, kernel)
	# opencvOutput = cv2.filter2D(gray, -1, kernel)

	#cv2.imshow("image", gray)
	cv2.imshow("image", convoleOutput)
	# cv2.imshow("image", opencvOutput)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
