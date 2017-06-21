#------------------------------------------------------Features Matching with opencv--------------------------------------

#Importing LIbraries

import numpy as np
import cv2
import matplotlib.pyplot as plt


#LOading IMages
img1 = cv2.imread('opencv-feature-matching-template.jpg',0)
img2 = cv2.imread('opencv-feature-matching-image.jpg',0)

#So far we've imported the modules we're going to use, and defined our two images, the template (img1) and the image we're going to search for the template in (img2).

orb = cv2.ORB_create()

#This is the detector we're going to use for the features.

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#Here, we find the key points and their descriptors with the orb detector.

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#This is our BFMatcher object.

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

#Here we create matches of the descriptors, then we sort them based on their distances.

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)

plt.imshow(img3,interpolation='bicubic')
plt.show()


#Wait for response
cv2.waitKey(0)

cv2.destroyAllWindows()


