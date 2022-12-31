import cv2
import time
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


pTime = 0

detector = htm.handDetector()

tipIds = [4, 8, 12, 16, 20]
x1= 0
y1= 0
x2= 0
y2= 0
x3= 0
y3= 0
x4= 0
y4= 0
d = 0.2
c = 0
a = 0


while True:
    success, img = cap.read()
    img= cv2.flip(img,1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    

    if len(lmList) != 0:
        fingers = []
        thump= lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]
        index=lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]
        middle= lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]
        ring= lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]
        pinky= lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]
     
 ##########################################################################################       
        #if thump==False and index==True and middle==False and ring==False and pinky==False :
            #print("index Up")         
###########################################################################################


        if thump==False and index==True and middle==False and ring==False and pinky==True and c==0 :
            c=c+1
            print("Point")
            x1= lmList[tipIds[1]][1]
            y1= lmList[tipIds[1]][2]
            time.sleep(d)
            
        
        elif thump==False and index==True and middle==False and ring==False and pinky==True and c==1 :
            c=c+1
            print("Point")
            x2= lmList[tipIds[1]][1]
            y2= lmList[tipIds[1]][2]
            time.sleep(d)
        

        elif thump==False and index==True and middle==False and ring==False and pinky==True and c==2 :
            c=c+1
            print("Point")
            x3= lmList[tipIds[1]][1]
            y3= lmList[tipIds[1]][2]
            time.sleep(d)
        
        elif thump==False and index==True and middle==False and ring==False and pinky==True and c==3 :
            c=c+1
            print("Point")
            x4= lmList[tipIds[1]][1]
            y4= lmList[tipIds[1]][2]
            time.sleep(d)
        
        elif thump==False and index==True and middle==True and ring==False and pinky==False :
            x1=0
            y1= 0
            x2=0
            y2= 0
            x3=0
            y3= 0
            x4=0
            y4= 0
            c=0
            
            

        cv2.circle(img, (x1, y1), 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x3, y3), 5, (0, 0, 0), cv2.FILLED)
        cv2.circle(img, (x4, y4), 5, (0, 255, 0), cv2.FILLED)
        if c==4:
            cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 5)
            cv2.line(img, (x2,y2), (x3,y3), (255,255,255), 5)
            cv2.line(img, (x3,y3), (x4,y4), (255,255,255), 5)
#-------------------------------------------------------------------------        
        ly1= y1-y2
        ly2= y2-y3
        ly3= y3-y4
#---------------------------------------------------------------------------        
        lx1= x1-x2
        lx2= x2-x3
        lx3= x3-x4
#---------------------------------------------------------------------------- 
   
        if ly1==0 and lx1==0  :

            a=0
              
        elif (ly1> 100 and lx1 <100 and x3==0 and y3==0 and x4==0 and y4==0) :
         
            a=1
            
        elif  (ly1 < -100 and lx1<100  and x3==0 and y3==0 and x4==0 and y4==0) :
           
            a=2
            
        elif (ly1 < -100 and lx1>100  and x3==0 and y3==0 and x4==0 and y4==0):
          
            a=3
           
        elif (ly1 < 100 and lx1<-100  and x3==0 and y3==0 and x4==0 and y4==0):
           
            a=4  

#---------------------------------------------------------------------------- 
     
        
        if ly2> 100 and lx2<100 and x4==0 and y4==0:
           
            a=1
           
        elif  ly2 < -100 and lx2<100 and x4==0 and y4==0:
           
            a=2
            
        elif ly2 < -100 and lx2>100 and x4==0 and y4==0:

            a=3
            
        elif ly2 < 100 and lx2<-100 and x4==0 and y4==0:
            
            a=4
           
    #---------------------------------------------------------------------------- 
     
        if ly3> 100 and lx3<100:
            
            a=1
        
        elif  ly3 < -100 and lx3<100 :
           
            a=2
           
        elif ly3 < -100 and lx3>100 :
           
            a=3
            
        elif ly3 < 100 and lx3<-100 :
            
            a=4
    #----------------------------------------------------------------------------         
        print (a )
    # #----------------------------------------------------------------------------    
        if a==0:
            cv2.putText(img, "Stop", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
        elif a==1:
            cv2.putText(img, "Move Forward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
        elif a==2:
            cv2.putText(img, "Move Backward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
        elif a==3:
            cv2.putText(img, "Move Left", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
        elif a==4:
            cv2.putText(img, "Move Right", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break