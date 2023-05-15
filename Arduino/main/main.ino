#include<Servo.h>
int xpos=90;
int ypos=90;
int sel = 0;
int inc =5;
Servo servoX;
Servo servoY;
//int pwmpin=6;
int i=0;
//int ledv=0;
//int ypos = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  servoX.attach(9);
  servoY.attach(11);
  //pinMode(pwmpin, OUTPUT);
  //pinMode(13, OUTPUT);
 // digitalWrite(13, HIGH);
 
  servoX.write(90);
  servoY.write(90);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    sel=Serial.parseInt();
    Serial.print(sel);
    if(sel==6){
      xpos= xpos+inc;
      servoX.write(xpos);
      

  }
  if(sel==4){
    xpos=xpos -inc;
    servoX.write(xpos);
  }
  if(sel==8){
    ypos=ypos -inc;
    servoY.write(ypos);
  }
  if(sel==2){
    ypos=ypos+inc;
    servoY.write(ypos);
  }
  
  
  }
  if(xpos<1){
    xpos =1;
  }
  if(xpos>180){
    xpos=180;
  }
  if(ypos<1){
    ypos =1;
    
  }
  if(ypos>180){
    ypos = 180;
  }
}
