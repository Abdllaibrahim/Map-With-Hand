import cv2
import time
import HandTrackingModule as htm

import serial
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


print("Start")
port="COM12" 
bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput() 
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
cf=0
cb=0
cr=0
cl=0
cs=0
cll=0
crr=0
cff=0
cfl=0 
cfr=0
cbb=0
clb=0
crb=0
clll=0
crrr=0

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
   
          
        if ly1==0 and lx1==0  :                                                         #Stop

            a=0
              
        elif (ly1> 100 and lx1 <100 and x3==0 and y3==0 and x4==0 and y4==0) :          #Forward
         
            a=1
            
        elif  (ly1 < -100 and lx1<100  and x3==0 and y3==0 and x4==0 and y4==0) :       #Backward
           
            a=2
            
        elif (ly1 < 50 and lx1>100  and x3==0 and y3==0 and x4==0 and y4==0):           #Left
          
            a=3
           
        elif (ly1 < 100 and lx1<-100  and x3==0 and y3==0 and x4==0 and y4==0):         #Right
           
            a=4  

#---------------------------------------------------------------------------- 
     
        
        if ly2> 100 and lx2<100 and x4==0 and y4==0 and ly1> 100 and lx1 <100: #Forward From Forward
           
            a=7
        
        elif ly2> 100 and lx2<100 and x4==0 and y4==0 and ly1 < 50 and lx1>100   : #Forward from left 
            a=8

        if ly2> 100 and lx2<100 and x4==0 and y4==0 and ly1 < 100 and lx1<-100   : #Forward from Right 
            a=9

        elif  ly2 < -100 and lx2<100 and ly1 < 50 and lx1>100 and x4==0 and y4==0: #Left Again
           
            a=5
        
        elif  ly2 < -100 and lx2<100 and ly1 < -100 and lx1<100 and x4==0 and y4==0: #Backward From Backward
           
            a=10

        elif  ly2 < -100 and lx2<100 and ly1 < 100 and lx1<-100 and x4==0 and y4==0: #Right Again
               
            a=6    
            
        # elif ly2 < 50 and lx2>100 and x4==0 and y4==0:  # Left

        #     a=3
        
        elif ly2 < 50 and lx2>100 and ly1 < -100 and lx1<100 and x4==0 and y4==0:  # Left Form Backward

            a=11
        
        elif ly2 < 50 and lx2>100 and ly1 < 50 and lx1>100 and x4==0 and y4==0:  # Left Form Left

            a=13
            
        # elif ly2 < 100 and lx2<-100 and x4==0 and y4==0:    #Right
            
        #     a=4

        elif ly2 < 100 and lx2<-100 and x4==0 and y4==0 and ly1 < 100 and lx1<-100:    #Right From Right
            
            a=14

        elif ly2 < 100 and lx2<-100 and x4==0 and y4==0 and ly1 < -100 and lx1<100:    #Right From Backward
            
            a=12
    #---------------------------------------------------------------------------- 
     
        if ly3> 100 and lx3<100 and ly2 < 50 and lx2>100: #Forward from left
            
            a=8
        
        elif ly3> 100 and lx3<100 and ly2 < 100 and lx2<-100: #Forward from Right
            
            a=9
        elif  ly3 < -100 and lx3<100 and ly2 < 50 and lx2>100 : #Left Again
           
            a=5

        elif  ly3 < -100 and lx3<100 and ly2 < 100 and lx2<-100:#Right Again
               
            a=6 

        # elif ly3 < 50 and lx3>100 :#Left
           
        #     a=3
        
        elif ly3 < 50 and lx3>100 and ly2 < 50 and lx2>100:#Left From Left
           
            a=13
        
        elif ly3 < 50 and lx3>100 and ly2 < -100 and lx2<100:#Left from Backward
           
            a=11
            
        # elif ly3 < 100 and lx3<-100 :#Right
            
        #     a=4
        
        elif ly3 < 100 and lx3<-100 and ly2 < 100 and lx2<-100:#RightFrom Right
            
            a=14


        elif ly3 < 100 and lx3<-100 and ly2 < -100 and lx2<100 :#Right From Backward
            
            a=12
    #----------------------------------------------------------------------------         
        print (a )
    # #----------------------------------------------------------------------------    
        if a==0:
            cv2.putText(img, "Stop", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cs=cs+1
            if cs==10:
                cs=0
                bluetooth.write(b"S")#These need to be bytes not unicode, plus a number

        elif a==1:
            cv2.putText(img, "Move Forward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cf=cf+1
            if cf==10:
                cf=0
                bluetooth.write(b"F")#These need to be bytes not unicode, plus a number
                
        elif a==2:
            cv2.putText(img, "Move Backward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cb=cb+1
            if cb==10:
                cb=0
                bluetooth.write(b"B")#These need to be bytes not unicode, plus a number
        elif a==3:
            cv2.putText(img, "Move Left", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cl=cl+1
            if cl==10:
                cl=0
                bluetooth.write(b"L")#These need to be bytes not unicode, plus a number
        elif a==4:
            cv2.putText(img, "Move Right", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cr=cr+1
            if cr==10:
                cr=0
                bluetooth.write(b"R")#These need to be bytes not unicode, plus a number

        elif a==5:
            cv2.putText(img, "Move Left again", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cll=cll+1
            if cll==10:
                cll=0
                bluetooth.write(b"LL")#These need to be bytes not unicode, plus a number
        elif a==6:
            cv2.putText(img, "Move Right again", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            crr=crr+1
            if crr==10:
                crr=0
                bluetooth.write(b"RR")#These need to be bytes not unicode, plus a number
    
        elif a==7:
            cv2.putText(img, "Forward From Forward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cff=cff+1
            if cff==10:
                cff=0
                bluetooth.write(b"FF")#These need to be bytes not unicode, plus a number
        
        elif a==8:
            cv2.putText(img, "Move Forward from left", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cfl=cfl+1
            if cfl==10:
                cfl=0
                bluetooth.write(b"FL")#These need to be bytes not unicode, plus a number

        elif a==9:
            cv2.putText(img, "Move Forward from Right", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cfr=cfr+1
            if cfr==10:
                cfr=0
                bluetooth.write(b"FR")#These need to be bytes not unicode, plus a number

        elif a==10:
            cv2.putText(img, "Move Backward Form Backward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            cbb=cbb+1
            if cbb==10:
                cbb=0
                bluetooth.write(b"BB")#These need to be bytes not unicode, plus a number

        elif a==11:
            cv2.putText(img, "Left from Backward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            clb=clb+1
            if clb==10:
                clb=0
                bluetooth.write(b"LB")#These need to be bytes not unicode, plus a number

        elif a==12:
            cv2.putText(img, "Move Right From Backward", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            crb=crb+1
            if crb==10:
                crb=0
                bluetooth.write(b"RB")#These need to be bytes not unicode, plus a number

        elif a==13:
            cv2.putText(img, "Left from Left", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            clll=clll+1
            if clll==10:
                clll=0
                bluetooth.write(b"LLL")#These need to be bytes not unicode, plus a number

        elif a==14:
            cv2.putText(img, "Move Right From Right", (45, 225), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 3)
            crrr=crrr+1
            if crrr==10:
                crrr=0
                bluetooth.write(b"RRR")#These need to be bytes not unicode, plus a number
  
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break