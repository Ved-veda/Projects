import cv2 as cv
haar_cascade =cv.CascadeClassifier('haar_face.xml')
capture = cv.VideoCapture(0)


while True:
    isTrue,frame = capture.read()
    
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors = 8)

    print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:

        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness = 2)
        
        cv.putText(frame,"FOUND A FACE",(x,y),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,255,0),1)


    cv.imshow("Faces DETECTED",frame)
    


    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows(0)