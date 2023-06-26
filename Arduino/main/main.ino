#include<Servo.h>
int xpos=90;
int ypos=90;
int sel = 0;
int inc =5;
Servo servo1;
Servo servo2;
Servo servo3;
//int pwmpin=6;
int i=0;
//int ledv=0;
//int ypos = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);
  //pinMode(pwmpin, OUTPUT);
  //pinMode(13, OUTPUT);
 // digitalWrite(13, HIGH);
 
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    sel=Serial.parseInt();
    Serial.print(sel);
    if(sel==6){
      xpos= xpos-inc;
      servo1.write(xpos);
      servo2.write(xpos);
      servo3.write(xpos);
  }
  if(sel==4){
    xpos = xpos+inc;
    servo1.write(xpos);
    servo2.write(xpos);
    servo3.write(xpos);
  }
  if(sel==8){
    ypos= ypos + inc;
    servo1.write(ypos);
    servo2.write(xpos);
    servo3.write(xpos);
  }
  if(sel==2){
    ypos= ypos - inc;
    servo1.write(ypos);
    servo2.write(xpos);
    servo3.write(xpos);
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
