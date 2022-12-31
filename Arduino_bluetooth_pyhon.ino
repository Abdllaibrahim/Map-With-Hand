#include "SoftwareSerial.h"
#define speedL 9
#define IN1 8
#define IN2 7
#define IN3 6
#define IN4 5
#define speedR 4
SoftwareSerial serial_connection(10,11);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar= -1;//Initialie the first character as nothing
int count=0;//This is the number of lines sent in from the python script
int i=0;//Arduinos are not the most capable chips in the world so I just create the looping variable once
int f=0, b=0, l=0, r=0, s=0, n=0, rr=0 ,ll=0 , ff=0, fl=0, fr=0, bb=0,lb=0, rb=0,lll=0, rrr=0;
void setup()
{
  for(int i=4 ; i<=9 ; i++)
{
pinMode(i, OUTPUT);
}
  
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
  pinMode(13,OUTPUT);
  
}

void forword()
{
digitalWrite(IN1, HIGH);
digitalWrite(IN2, LOW);
digitalWrite(IN3, HIGH);
digitalWrite(IN4, LOW);
analogWrite(speedL,255);
analogWrite(speedR,140);
}
void backword()
{
digitalWrite(IN1, LOW);
digitalWrite(IN2, HIGH);
digitalWrite(IN3, LOW);
digitalWrite(IN4, HIGH);
analogWrite(speedL,150);
analogWrite(speedR,150);
}

void left()
{
digitalWrite(IN1, LOW);
digitalWrite(IN2, LOW);
digitalWrite(IN3, HIGH);
digitalWrite(IN4, LOW);
analogWrite(speedL,0);
analogWrite(speedR,150);
}
void right()
{
digitalWrite(IN1, HIGH);
digitalWrite(IN2, LOW);
digitalWrite(IN3, LOW);
digitalWrite(IN4, LOW);
analogWrite(speedL,150);
analogWrite(speedR,0);
}

void stopp() {
digitalWrite(IN1, LOW);
digitalWrite(IN2, LOW);
digitalWrite(IN3, LOW);
digitalWrite(IN4, LOW);
analogWrite(speedL,0);
analogWrite(speedR,0); }
void loop()
{
  //This will prevent bufferoverrun errors
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script
  if(byte_count)//If there are any bytes then deal with them
  {
    Serial.println("Incoming Data");//Signal to the monitor that something is happening
    int first_bytes=byte_count;//initialize the number of bytes that we might handle. 
    int remaining_bytes=0;//Initialize the bytes that we may have to burn off to prevent a buffer overrun
    if(first_bytes>=BUFFER_SIZE-1)//If the incoming byte count is more than our buffer...
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);//Reduce the bytes that we plan on handleing to below the buffer size
    }
    for(i=0;i<first_bytes;i++)//Handle the number of incoming bytes
    {
      inChar=serial_connection.read();//Read one byte
      inData[i]=inChar;//Put it into a character string(array)
    }
    inData[i]='\0';//This ends the character array with a null character. This signals the end of a string
    // =================================================================================================================================================
    if(String(inData)=="F" && f==0)//This could be any motor start string we choose from the python script
    {
      //Serial.println("Forward");
      forword();
      delay(1000);
      stopp();
      f=1;b=0; l=0;  r=0; s=0; rr=0; ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
    //---------------------------------------------------------------------------------------------------------------------------------------------
    else if(String(inData)=="B" && b==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Backward");
     backword();
     delay(1000);
     stopp();
      f=0;b=1; l=0;  r=0; s=0;  rr=0; ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
     
    }
    
    //--------------------------------------------------------------------------------------------is is an arbitrary choice. It would probably be something like: MOTOR_STOP
   
     else if(String(inData)=="L" && l==0)//Again th
   {
      //Serial.println("Left");
      left();
      delay(1000);
      forword();
      delay(1000);
      stopp();
       l=1;
       b=0; f=0;  r=0; s=0;  rr=0;  ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
    
    //---------------------------------------------------------------------------------------------------------------------------------------------
       else if(String(inData)=="R" && r==0)//Again th
   {
      //Serial.println("Right");
      right();
      delay(1000);
      forword();
      delay(1000);
      stopp();
       r=1;
       b=0; l=0;  r=1; s=0;  rr=0;  ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
     //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="RR" && rr==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Right");
     right();
     delay(1000);
     forword();
     delay(1000);
     stopp();
      f=0;b=0; l=0;  r=0; s=0;     rr=1;     ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
   //--------------------------------------------------------------------------------------------------------------------------------------------- 
    else if(String(inData)=="LL" && ll==0)//Again th
   {
      //Serial.println("Left");
      left();
      delay(1000);
      forword();
      delay(1000);
      stopp();
     f=0;     b=0;    l=0;  r=0;        s=0;       rr=0;      ll=1;ff=0; fl=0;  fr=0; bb=0 ; lb=0; rb=0;lll=0; rrr=0;
    }
    
    //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="S" && s==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Stop");
      stopp();
      delay(100);
       f=0;     b=0;    l=0;  r=0;        s=1;   ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
    //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="FF" && ff==0)//This could be any motor start string we choose from the python script
    {
      //Serial.println("Forward");
      forword();
      delay(1000);
      stopp();
      f=0;     b=0;    l=0;  r=0;        s=0;  rr=0; ll=0;ff=1, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
    //---------------------------------------------------------------------------------------------------------------------------------------------
    else if(String(inData)=="FL" && fl==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Right");
     right();
     delay(1000);
     forword();
     delay(1000);
     stopp();
      f=0;     b=0;    l=0;  r=0;        s=0;    rr=0;   ll=0;ff=0, fl=1, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
     //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="FR" && fr==0)//Again th
   {
      //Serial.println("Left");
      left();
      delay(1000);
      forword();
      delay(1000);
      stopp();
       f=0;     b=0;    l=0;  r=0;        s=0;    rr=0;  ll=0;ff=0, fl=0, fr=1, bb=0,lb=0, rb=0;lll=0, rrr=0;
    }
    
    //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="BB" && bb==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Backward");
     backword();
     delay(1000);
     stopp();
    f=0;     b=0;    l=0;  r=0;        s=0;   rr=0; ll=0;ff=0, fl=0, fr=0, bb=1,lb=0, rb=0;lll=0, rrr=0;
     
    }
    //--------------------------------------------------------------------------------------------------------------------------------------------------
    else if(String(inData)=="LB" && lb==0)//Again this is an arbitrary choice. It would probably be something like: MOTOR_STOP
    {
      //Serial.println("Right");
     right();
     delay(1000);
     forword();
     delay(1000);
     stopp();
      f=0;     b=0;    l=0;  r=0;        s=0;   rr=0;   ll=0;ff=0, fl=0, fr=0, bb=0,lb=1, rb=0;lll=0, rrr=0;
    }
     //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="RB" && rb==0)//Again th
   {
      //Serial.println("Left");
      left();
      delay(1000);
      forword();
      delay(1000);
      stopp();
   f=0;     b=0;    l=0;  r=0;        s=0;   rr=0;  ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=1;lll=0, rrr=0;
      
    }
    //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="LLL" && lll==0)//Again th
   {
     
      forword();
      delay(1000);
      stopp();
      f=0;     b=0;    l=0;  r=0;        s=0;   rr=0;  ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=1, rrr=0;
   }
    //---------------------------------------------------------------------------------------------------------------------------------------------
     else if(String(inData)=="RRR" && rrr==0)//Again th
   {
     
      forword();
      delay(1000);
      stopp();
    f=0;     b=0;    l=0;  r=0;        s=0;    rr=0;  ll=0;ff=0, fl=0, fr=0, bb=0,lb=0, rb=0;lll=0, rrr=1;
   }
      //---------------------------------------------------------------------------------------------------------------------------------------------
      
      
    for(i=0;i<remaining_bytes;i++)//This burns off any remaining bytes that the buffer can't handle.
    {
      inChar=serial_connection.read();
    }
    Serial.println(inData);//Print to the monitor what was detected
    serial_connection.println("Hello from Blue "+String(count));//Then send an incrmented string back to the python script
    count++;//Increment the line counter
  }
  delay(100);//Pause for a moment 
}
