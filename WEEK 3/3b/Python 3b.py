import serial
from time import sleep

ser = serial.Serial('COM3', 9600)
sleep(5)

print("Enter a number between 0-180, or 'e' to exit the program\n")

enter = input()


while enter != 'e':

   
   if(int(enter) >= 0 and int(enter) <= 180):

      
      ser.write(str(enter).encode())

      
      print("I have sent: " + str(enter))

   
   else:
      print("Enter a number between 0-180, or 'e' to exit")

   
   print("Enter a number between 0-180: ")
   enter = input()
