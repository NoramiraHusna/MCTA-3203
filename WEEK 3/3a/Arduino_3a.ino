int analogPin = 0;     
int data = 0;           
char userInput;
#define LED_PIN 9
void setup(){
  pinMode(LED_PIN,OUTPUT);
  Serial.begin(9600);                        //  setup serial

}

void loop(){
int potentiometerValue = analogRead(analogPin);
  int brightness = potentiometerValue / 4;
  analogWrite(LED_PIN, brightness);
   Serial.println(potentiometerValue);
   delay (100);

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'g'){                  // if we get expected value 

            data = analogRead(analogPin);    // read the input pin
            Serial.println(data);            
            
      } // if user input 'g' 
  } // Serial.available
} // Void Loop