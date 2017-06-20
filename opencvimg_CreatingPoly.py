#--------------------------------Creating Patterns and text on Image Feeds------------------------------------

#Loading Modules

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

#Loading Image feeds.

img=cv2.imread('Loaction of the image',cv2.IMREAD_COLOR) #lOADING THE IMAGE IN COLOR MODE.

#For pattern Boundaries different type of color format is required  for the detection process:
	#white=(B,G,R)=(225,225,225)
	#blue=(B,G,R)=(225,0,0)
	#green=(B,G,R)=(0,225,0)
	#red=(B,G,R)=(0,0,225)


#For creation of a simple 2D line

starting_coordinate=(,)
destination_coordinate=(,)
color=('B_VALUE','G_VALUE','R_VALUE')
linewidth=#15/as you like.

cv2.line(img,starting_coordinates,destination_coordinates,color,linewidth)

#For Creating a rectagular pattern

topleft_coordinates=(,)
bottomright_coordinates=(,)
linewidth=#repplace with the values.
color=('B_VALUES','G_VALUES','R_VALUES')


cv2.rectangle(img,topleft_coordinates,bottomright_coordinates,color,linewidth)


#For creating an circle filled_in/filled_out

centre_coordinates=(,)
radius_value=#replace comments with the values.
color=('B_VALUE','G_VALUE','R_VALUE')
filled_in/filled_out=1/-1

cv2.circle(img,centre_coordinates,radius_value,color,'filled_in/filled_out value')


#For construction of a polygon

#creating a bunch of points
pts=np.array([[,],[,],[,],[,],[,]],np.int32)

#always rehape the points.for details read the official documents
pts=pts.reshape((-1,1,2))


color=('B_VALUE','G_VALUE','R_VALUE')
cv2.polyines(img,[pts],True,color,1)


#Writing Text on the image Feed
Font=#select the officila OpenCv fonts for the text
#eg:-
font=cv2.FONT_HERSHEY_SIMPLEX
starting_coordinates=(,)
size=#1/2/3/4/5/6.....
color=('B_VALUE','G_VALUE','R_VALUE')
thickness_value=#add values

cv2.puttext(img,'REQUIRED_TEXTS',starting_coordinates,font,size,color,thickness_value,cv2,LINE_AA)


cv2.imshow("Title",img)#Displaying processed Image

cv2.waitKey(0)#Wait key to be pressed

cv2.write("title_to_be_saved_with_dest.",img)#save processed imge to  a location

cv2.destroyAllWndows()#Close all Formatted windows.


