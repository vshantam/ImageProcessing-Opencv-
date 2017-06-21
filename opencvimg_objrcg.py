#-----------------------------------------------------Facial and Eye detection using Haarcascade Datasets-------------------------------------------

#importing Libraries
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

#importing Haarcascade datasets
face_cascade=cv2.CascadeClassifier(' ')#copy the locations
eye_cascade=cv2.CascadeClassifier(' ')#copy the locations

#importing the image adn conversion to grayscale
img=cv2.imread('',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#detection of face and eye

faces=face_cascade.detectMultiScale(gray,1.3'''quality''',3'''seperation''')


'''Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once we get these locations, we can create a ROI for the face and apply eye detection on this ROI (since eyes are always on the face !!! ).'''


for (x,y,w,h) in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
	roi_gray=gray[x:x+w,y:y+h]
	roi_color=img[x:x+w,y:y+h]
	eyes=eye_cascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectange(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),4)


#Displaying IMages
cv2.imshow("Detected IMage")

#Waiting for responses
cv2.waitKey(0)

cv2.destroyAllWindows()
