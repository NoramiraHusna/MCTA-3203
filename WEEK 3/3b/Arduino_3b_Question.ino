#include <Servo.h>

Servo myservo;
int potPin = A0;
int potValue = 0;
int angle = 0;
unsigned long previousMillis = 0;
const long interval = 100; // Adjust as needed

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  // Read the potentiometer value
  potValue = analogRead(potPin);
  
  // Map the potentiometer value to servo angle (0 to 180)
  angle = map(potValue, 0, 1023, 0, 180);
  
  // Send servo angle to Python over serial
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    Serial.println(angle);
    previousMillis = currentMillis;
  }
  
  // Read from serial for halt command
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'H' || command == 'h') {
      while (Serial.available() > 0) Serial.read(); // Clear serial buffer
      while (true) {} // Halting execution
    }
  }

  // Set servo angle
  myservo.write(angle);

  // Some delay for stability
  delay(10);
}
