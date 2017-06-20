#---------------------------------------------------Loading Image and the corner Detection test-------------------------------------------------

#Importing Modules

import numpy as np
import os
import matplotlib.pyplot as plt
import cv2


#Loading mage in Opencv Memory for Processing
img=cv2.imread('Image Location',cv2.IMREAD_COLOR)


#image should be colorless for this process.
#convertimg image to grey color image.(Removing ALPHA)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#converting to floating point.
gray=np.float32(gray)

#Applying the cornerdetection algorithm

corners=cv2.goodFeaturesToTrack(gray, 100,0.01,6)#Parameters are image,number of corner to be displayed,corner quality,distances between  corner dots.
corners=np.int0(corners)

#Arranging the corner position.
for corner in corners:
	x,y=corner.ravel()#providing corner coordinates.
	
	#Corner will be displayed using circle dots
	cv2.circle(img,(x,y),5,(255,0,0),-1)
				#B,G,R

#Displaying processd image with the corners detected.
cv2.imshow("Image_with_Detected_Corners",img)


#Wait for kay to be pressed.
cv2.waitKey(0)

#Kill all The windows generated during the process
cv2.destroyAllWindows()

