import serial

ser = None

try:
    ser = serial.Serial( "COM3", 9600, timeout=0.05)
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(data)
except Exception as e:
    print("Error:", e)
finally:
    if ser is not None and ser.is_open:
        ser.close()
