# Essential OpenCV functions for image processing and manipulation
import cv2 as cv

# Reading Images
image = cv.imread('OpenCV_studying/Resources/Photos/park.jpg')
cv.imshow('Park',image)

# Converting to grayscale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur = cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# # Edge Cascade
# canny = cv.Canny(image,125,175) # 125 ve 175 threshold değerleridir
# cv.imshow('Canny Edges',canny)

# # Dilating the image
# dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('Dilated',dilated)



cv.waitKey(0)
