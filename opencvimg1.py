#--------------------------Vedio Feed usng OpenCv ------------------------------------

#Required Modules

import numpy as np
import cv2
import os

'''The OPenCv performs same operation to feed whether it is an image or Vedio.The way vedio works is with THe frames per sec (FPS) and each frame is still an image so it is basically the same thing or we can say that Looping the continuos capturing of image leads to the formation of images.'''

#For primary   Webcam Feed :- 0
#For secondary Webcam Feed :- 1

#Capturing Images.
cap=cv2.VedioCapture(0) #For Primary webcam

#To use recoded vedio as a feed 
'''cap=cv2.VedioCapture('Location of the vedio')'''


#To save each frames 
fourcc=cv2.VedioWriter("Output_name.avi",fourcc,20.0,(720,640))#(720,640)==720x640 pixel values.It depends on the Webcam quality.

#Looping the continuos caption .

while True:
	ret,frame=cap.read()

	#For changing the Background color of the Vedio feeds.
	grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GREY) #will display another window with same vedio feed but grey in color .You can always use different 								option and for that refer the official Documentations.
	cv2.imshow("Grey Title",grey)
	cv2.imshow("Title",frame)

	out.write(frame)

	if cv2.waitKey(1) &  0xFF=='q':
		break

cap.release()

out.release()

cv2.destroyAllWindows()

