#------------------------------------------------Gradient and edge detection using opencv-------------------------------------------------------


#importing Modules
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2




#Feeding image and Grayscale conversion
img=cv2.imread('',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Processing image for the Laplaian form
laplace=cv2.Laplacian(gray,cv2.CV_64F)


#implementing processed image for Display using matplotlib
plt.imshow(laplace,interpolation='bicubic')
plt.show()

#Implementing using opencv
cv2.imshow("title",laplace)

#Implementing image gradient in vertically and horizontly
soblex=cv2.Sobel(gray,cv2.CV_64F,1,0,15)  #Values must not be grater then 30
		      #Dtat_type  #x,y,value

'''similarly in vertically'''

sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,15)


#Finally the edge detection of the processd Image

valuex=100
valuey=100
edge=cv2.Canny(gray,valuex,valuey)#canny edge detection Algorithm
'''Values cant be changed depending on the image quality and noise in the channels'''


#Displaying Images
cv2.imshow("Origional",img)
cv2.imshow("Laplacian",laplace)
cv2.imshow("Gradient X",sobelx)
cv2.imshow("Gradient Y",sobely)
cv2.imshow("Edge Removed",edge)

#waiting for the response
cv2.waitKey(0)

#kill all windows
cv2.destroyAllWindows()


