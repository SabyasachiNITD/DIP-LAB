import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def convo(img,kernel):
	imageH,imageW = img.shape
	kernelH,kernelW = kernel.shape
	pad=1
	image =cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_REPLICATE)

	returnimg = np.zeros((imageH,imageW) , dtype = "float32")

	for y in np.arange(pad,imageH+pad):
		for x in np.arange(pad,imageW+pad):
			newy1 = y-pad
			newy2 = y+pad+1
			newx1 = x-pad
			newx2 = x+pad+1
			roi = image[newy1:newy2,newx1:newx2]
			k = (roi*kernel).sum()
			returnimg[y-pad,x-pad] = k
	return returnimg


if __name__=="__main__":
	image = cv2.imread("1.tif",0)
	kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]],dtype="int")
	output = convo(image,kernel)
	cv2.imshow("Horiontal Edging",output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()





