import cv2 as cv

# Görüntüyü yükle
image = cv.imread('OpenCV_studying/Resources/Photos/park.jpg')
cv.imshow('Orijinal Görüntü', image)

# Gri tonlamalıya çevir
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gri Tonlama', gray)

# Gaussian Blur uygulama
blur = cv.GaussianBlur(gray, (5, 5), 0)
cv.imshow('Bulaniklastirilmis image', blur)

# Kenar tespiti
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

canny_low = cv.Canny(blur, 50, 100)  # Daha fazla kenar tespit edilir.
canny_high = cv.Canny(blur, 200, 250)  # Daha az ama kesin kenarlar tespit edilir.
# cv.imshow('Canny Low Edges', canny_low)
# cv.imshow('Canny High Edges', canny_high)

dilated = cv.dilate(canny, (9,9), iterations=3)
cv.imshow('Dilated', dilated)


cv.waitKey(0)
cv.destroyAllWindows()
