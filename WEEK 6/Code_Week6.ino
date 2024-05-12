float tempcelc;
int ldr_value;
int ldr_percent;
int lm_value;

void setup() {
  Serial.begin(9600);
  Serial.println("CLEARDATA");
  Serial.println("LABEL, TIME, TEMPERATURE, LIGHT "); // Updated label
}

void loop() {
  lm_value = analogRead(A0);
  tempcelc = (lm_value / 1023.0) * 5000.0;
  tempcelc = tempcelc / 10.0;

  ldr_value = analogRead(A1);

  Serial.print("DATA, TIME, ");
  Serial.print(tempcelc);
  Serial.print(","); // Separating temperature and light values with a comma
  Serial.println(ldr_value);

  delay(1500);
}