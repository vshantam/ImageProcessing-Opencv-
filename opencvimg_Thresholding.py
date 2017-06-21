#--------------------------------------------------THRESHOLDING OF THE IMAGE WITH OPENCV---------------------------------------------------

'''For different types of thresholding prese refer the origional documentation.THresholding on image is used to perform clarification on specific regions.Few basics thresholdings are being used in this .'''



#importing Modules
import os,numpy as np,matplotlib.pyplot as plt,cv2

#Loading Image with grayscaled
img=cv2.imread('',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Applying Threholding with a reteurn value
minval=#
maxval=#
retval,threshold=cv2.Threshold(gray,minval,maxval,cv2.THRESH_BINARY)#simple binary Conversion

#Adaptive Thresholding(Gaussian)
maxval=#
retval1,threshold1=cv2.adaptiveThreshold(gray,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY)

#OTSU thresholding

maxval=#
minval=#
retval2,threshold2=cv2.threshold(gray,minval,maxval,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#Displaying All the threshold processed images

cv2.imshow("title1",img)

cv2.imshow("title2",threshold)

cv2.imshow("title3",threshold1)

cv2.imshow("title4",threshold2)


#wait for response
cv2.waitKey(0)

cv2.destroyallWindows()
