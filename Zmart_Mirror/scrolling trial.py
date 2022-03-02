
import cv2 as cv


img1 = cv.imread(r'C:\Users\DTG\Desktop\Coding lol\Python 2022\Opencv python\Sample pics+vids\trial1.jpg')

def rescaleFrame(frame,scale = 3):
    #the function takes a frame and 
    #the width and height are scaled to be 0.75 times the orignials
    width =int( frame.shape[1]*scale )
    height = int(frame.shape[0]*scale)
    
    #passes the dimenions as a tuple
    dimensions = (width,height)
    
    #resizes the fame to a particular dimension 
    #returns a tuple containing the frame info,dimensions info and the resized data
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

'''
def gsc(frame):
    width =int( frame.shape[1])
    height = int(frame.shape[0])
    #passes the dimenions as a tuple
    dimensions = (width,height)
    return dimensions
 
resized = rescaleFrame(img1)

print("New : ",gsc(resized))

x = 0
y = 0 

while x < gsc(resized)[0] and y < gsc(resized)[1] :
        cv.putText(rescaleFrame(img1),"scrolling ? ",(x,y),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
        
        cv.imshow('text',resized)
        

        x+=1
        y+=1

while True:
    cv.imshow('without scroll', resized)

    

    if cv.waitKey(20) & 0xFF == ord('d'):
        cv.destroyAllWindows()
  
  '''






x = 0
capture = cv.VideoCapture(0)
def rescaleFrame(frame,scale = 1):
    #the function takes a frame and 
    width =int( frame.shape[1]*scale )
    height = int(frame.shape[0]*scale)
    
    #passes the dimenions as a tuple
    dimensions = (width,height)
    
    #resizes the fame to a particular dimension 
    #returns a tuple containing the frame info,dimensions info and the resized data
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

list1 = ['a','b','c','d','e','f','g','h']
list2 = []
for i in list1:
    for j in range(8):
        list2.append("*")
        list2.append(i)    

x = 0
while x < len(list2): 
    
    for i in range(2):
        isTrue, frame = capture.read() 
        cv.imshow('webcam original',frame)  
        resized = rescaleFrame(frame)
           
        cv.putText(resized,list2[x],(50,50),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
            
        cv.imshow('mod',resized)

                    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break 
    x+=1        

    if x == len(list2) :
        x=0

capture.release() 
cv.destroyAllWindows(0)    
cv.waitKey(0)








'''
# Aniamted rectangle
import cv2
import numpy as np
import time

Frame_out = np.zeros((500, 640, 3),np.uint8)
a = 1
while a<255:
    cv2.rectangle(Frame_out,(a,a),(a*2,a*2),(0,0,255-a),0)
    time.sleep(0.05)
    cv2.imshow("Animation", Frame_out)
    cv2.rectangle(Frame_out,(a,a),(a*2,a*2),(0,0,0),0)
    a +=2
    if(a > 254):
        a = 1
    k = cv2.waitKey(10)
    if k == 27:
        break

cv2.destroyAllWindows()
'''