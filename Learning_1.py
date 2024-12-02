import cv2 as cv

# img = cv.imread('OpenCV_studying/Resources/Photos/cat.jpg')

# cv.imshow('Cat',img)

# capture = cv.VideoCapture(0) 

# cv.imshow('Video',capture) # Videoyu göstermez

capture = cv.VideoCapture('OpenCV_studying/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(10) & 0xFF==ord('d'):# Burası 10 ms bekler ve 'd' tuşuna basılırsa döngüyü kırar
        break


# 0 girilirse sonsuza kadar bekler
# 1 girilirse 1 ms bekler
# 1000 girilirse 1 saniye bekler 
cv.waitKey(0) 
