import cv2
import time
import matplotlib.pyplot as plt
#import pyrebase
#config = {
#  "apiKey": "AIzaSyCt7Q0S7H_cuaspK6gXB7dVeX0xD1RNfYU",
#  "authDomain": "pytest-214109.firebaseapp.com",
 # "databaseURL": "https://pytest-214109.firebaseio.com",
  #"storageBucket": "pytest-214109.appspot.com",
  #"serviceAccount": "/Users/SAKSHIM/Documents/python/pyrebase/pytest-214109-2fcef3c3ba83.json"
#  "messagingSenderId": "325355378495"
#}
#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
#user = auth.sign_in_with_email_and_password("fileindie@gmail.com", "saksneh098")
#user = auth.refresh(user['refreshToken'])
#db = firebase.database()

backsub = cv2.createBackgroundSubtractorMOG2()
cap = cv2.VideoCapture("C:/Users/ASUS/Desktop/video/tr2.mp4") #Path of the source video || Change if you want to test with your own video
i = j = c = 0
ret, frame = cap.read()
im=plt.imshow(frame, interpolation='none')
plt.ion()
minArea = 1
while True:
    ret, frame = cap.read()
    fgmask = backsub.apply(frame, None, 0.01)  
    if fgmask is None:
        break                                    
    erode = cv2.erode(fgmask,None,iterations=2)     
    moments = cv2.moments(erode,True)              
    area = moments['m00']
    cv2.line(frame, (150,250), (297,250), (0,0,255), 5)
    cv2.line(frame, (375,250), (530,250), (0,0,255), 5)

    if area >= minArea:
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        
        if(c == 0):
            if x > 150 and x < 250 and y > 249 and y < 297: #range of co-ordinates for objects in left lane
                i = i+1
                c = 8
                cv2.line(frame, (150,250), (297,249), (0,255,0), 5)
 #               data={"time": time.time(), "count_l":i}
 #               res=db.child("place").child("1234").push(data, user['idToken'])
 #               print(i)
            
            elif x > 461 and x < 558 and y > 299 and y < 355:#range of co-ordinates for objects in right lane
                j = j+1
                c = 8
                cv2.line(frame, (375,250), (530,250), (0,255,0), 5)
 #               data={"time": time.time(), "count_r":j}
 #               res=db.child("place").child("1234").push(data, user['idToken'])
 #               print(j)
        else:
            c = c-1
            continue
        
            
    cv2.putText(frame, 'Left Lane: %r' %i, (10,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 255, 0), 2)
    cv2.putText(frame, 'Right Lane: %r' %j, (380,30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 2)
        
    key = cv2.waitKey(30)
    
    if  key == ord('p'):
        while True:
            key2 = cv2.waitKey(0)
            if key2 == ord('p'):
                break
    im.set_data(frame)
    plt.pause(0.01)
    cv2.imshow("Traffic Video Feed", frame)
    cv2.imshow("Foreground Mask", fgmask) #Eliminated static background, only the moving part of the video is considered
    if key == ord('q'):
            break

plt.ioff()
plt.show(False)
cv2.destroyAllWindows() #close the program
