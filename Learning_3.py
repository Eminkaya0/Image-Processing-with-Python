# Drawing shapes and writing text on images using OpenCV

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') # dtype='uint8' means that the image is going to be 8 bit unsigned integer

#imread yapmana gerek yok çünkü zaten blank bir resim oluşturuyoruz
# cv.imshow('Blank',blank) # Blank image

# 1. Paint the image a certain color
# blank[200:300,300:400] = 0,255,0 # Green
# cv.imshow('Green',blank)

# 2. Draw a Rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)# -1 doldurur 
# cv.rectangle(blank,(0,0),blank.shape[1]//2,(0,255,0),thickness=2) de olabilirdi.
# cv.imshow('Rectangle',blank)

# 3. Draw a Circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# 5. Write Text
cv.putText(blank,'Hello, my name is Emin',(0,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,255),2,cv.LINE_AA)
cv.imshow('Text',blank)
# Create a blank image
# img = cv.imread('OpenCV_studying/Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

cv.waitKey(0)