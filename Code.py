import cv2
backsub = cv2.bgsegm.createBackgroundSubtractorMOG()
cap = cv2.VideoCapture("C:/Users/ASUS/Desktop/video/tr2.mp4") 
i = j= c= 0
minArea=1
while True:
    ret, frame = cap.read()
    fgmask = backsub.apply(frame, None, 0.01)  
    if fgmask is None:
        break                                    
    erode=cv2.erode(fgmask,None,iterations=2)     
    moments=cv2.moments(erode,True)              
    area=moments['m00'] 
    
    if area >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        
        if(c==0):
            if x>150 and x<160 and y>250 and y<296 or (x>240 and x<249 and y>249 and y<297): #range of co-ordinates for objects in left lane
                i=i+1
                c=4
                print(i)
            
            elif x>552 and x<558 and y>299 and y<355 or( x>461 and x<470 and y>325 and y<335):#range of co-ordinates for objects in right lane
                j=j+1
                c=4
                print(j)
        else:
            c=c-1  
            continue  
        
            
    cv2.putText(frame,'Left Lane: %r' %i, (10,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 255, 0), 2)
    cv2.putText(frame,'Right Lane: %r' %j, (380,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 2)
        
    key = cv2.waitKey(50)
    
    if  key== ord('p'):  #Press P to pause video
        while True:
            key2=cv2.waitKey(0)
            if key2==ord('p'):
                break
    cv2.imshow("Traffic Video Feed", frame)
    cv2.imshow("Foreground Mask", fgmask)
    if key == ord('q'):    #Press Q to quit
            break
cv2.destroyAllWindows()      

