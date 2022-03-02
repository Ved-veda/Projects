from bs4 import BeautifulSoup as bs
import requests
import cv2 as cv
import time



# getting the just in news from The Hindu site
source = requests.get("https://www.thehindu.com/news/").text
soup = bs(source,'lxml')

#parsing the html doculment and scrapping the site for relevent info
news = []
animate = []
for strings in soup.stripped_strings:
    if len(strings) > 50 and "Watch" not in strings:
        news.append(strings)
del news[0]        

for i in news:
    i = i + '.'
    for z in range(40):
        animate.append("#")
        
    if len(i) > 50:
            l = i.split()
            half = int(len(l)/2)
                    
            string1 = ''
            for z in range(half):
                string1 = string1 + ' ' + l[z] 
            for op in range(40):
                animate.append(string1)
                
            string2 = ''
            for z in range(half,len(l)):
                string2 = string2 + ' ' + l[z]
            for op in range(40):
                animate.append(string2)    

    else:
        for op in range(40):
            animate.append(i)

def rescaleFrame(frame,scale = 1.25):
    #the function takes a frame and 
    width =int( frame.shape[1]*scale )
    height = int(frame.shape[0]*scale)
    
    #passes the dimenions as a tuple
    dimensions = (width,height)
    #resizes the frame to a particular dimension 
    #returns a tuple containing the frame info,dimensions info and the resized data

    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA),dimensions
    

capture = cv.VideoCapture(0)
x = 0
while x < len(animate):

    isTrue, frame = capture.read() 
          
    resized,d = rescaleFrame(frame)
        
           
    cv.putText(resized,animate[x],(10,35),cv.FONT_HERSHEY_TRIPLEX,0.65,(0,255,0),2)

     

    cv.putText(resized,str(time.asctime()),(10,580),cv.FONT_HERSHEY_TRIPLEX,0.65,(255,255,255),2)

        #rectangle method
        # rectangle(image,point1,point2,colour,thickness and line type)
    cv.rectangle(resized,(1,1),d,(0,255,0),thickness = 3)

    cv.imshow('mod',resized)
        
                    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break 
    x+=1        

    if x == len(animate) :
        x=0

capture.release() 
cv.destroyAllWindows(0)    
cv.waitKey(0)


