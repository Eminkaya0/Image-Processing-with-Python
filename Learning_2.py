
# Resizing and Rescaling Frames in OpenCV

import cv2 as cv

image = cv.imread('OpenCV_studying/Resources/Photos/cat.jpg')
 
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)# Normalde float döndürür ama int döndürmek istediğimiz için int() fonksiyonunu kullandık 
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    # Resize the frame 
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def ChangeRes(width,height):
    # Live video için çalışır
    capture.set(3,width)
    capture.set(4,height)

# Reading Images
cv.imshow('Cat',image)
cv.imshow('Cat Resized',rescaleFrame(image))


# Reading Videos
capture = cv.VideoCapture('OpenCV_studying/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    

    frame_resized = rescaleFrame(frame,scale=0.1)    
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):# Burası 10 ms bekler ve 'd' tuşuna basılırsa döngüyü kırar
        break


cv2.waitKey(0) # 0 means that the window will be closed when any key is pressed