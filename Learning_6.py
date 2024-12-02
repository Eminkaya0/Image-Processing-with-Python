import cv2 as cv
import numpy as np

# Görüntüyü yükle
# Görüntüyü yükle
img = cv.imread('OpenCV_studying/Resources/Photos/park.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Kenar tespiti (opsiyonel)
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

# Kontur tespiti
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Kontur çizimi
blank = np.zeros_like(img)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()
