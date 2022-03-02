import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    
    ret,thresh1 = cv.threshold(gray, 200, 255, cv.THRESH_TOZERO)

    blur = cv.GaussianBlur(thresh1,(35,35),cv.BORDER_DEFAULT)


    (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(blur)

    cv.circle(frame, maxLoc, 25, (255, 0, 0), 2)
    cv.circle(thresh1, maxLoc, 25, (255, 0, 0), 2)
    cv.circle(blur, maxLoc, 25, (255, 0, 0), 2)
    
    
    cv.imshow("Brightest",frame)
    cv.imshow('thresh processing',thresh1)
    cv.imshow('blur processing',blur)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows(0)