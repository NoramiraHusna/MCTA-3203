#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
}

void loop() {
  int16_t ax, ay, az, gx, gy, gz; // Define variables to store sensor readings
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); // Corrected function call

  Serial.print("Accel: ");
  Serial.print(ax);
  Serial.print(", ");
  Serial.print(ay);
  Serial.print(", ");
  Serial.print(az);
  Serial.print(" Gyro: ");
  Serial.print(gx);
  Serial.print(", ");
  Serial.print(gy);
  Serial.print(", ");
  Serial.println(gz);

  delay(250); // Adjust the delay as needed
}