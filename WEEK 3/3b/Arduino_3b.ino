#include <Servo.h>

#define SER 9 

 

Servo servo; 

int mssg; 

  

void setup()

{

   

   servo.attach(SER);

   Serial.begin(9600);

}

  

void loop()

{

   if (Serial.available() > 0)

   {

     mssg = Serial.parseInt(); 

     servo.write(mssg); 

     delay(50);

   }

}