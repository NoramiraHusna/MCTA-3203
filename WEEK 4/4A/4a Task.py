import serial
import time

# Define the serial port and baud rate
serial_port = 'COM7'  # Change this to your Arduino's serial port
baud_rate = 9600

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def detect_gesture(ax, ay, threshold):
    # Define conditions to recognize specific gestures
    if ay > 145:
        return "Gesture 2: Up"
    elif ay < 80:
        return "Gesture 1: Down"
    elif ax > 155:
        return "Gesture 3: Left"
    elif ax < 80:
        return "Gesture 4: Right"
    elif 100 < ax < 170 and 80 < ay < 130:
        return "Gesture 5: initial"
    else:
        return "No Gesture Detected"

try:
    while True:
        # Read data from Arduino
        data = ser.readline().decode().strip()
        print("Received data:", data)  # Print received data for debugging
        # Split the data into accelerometer and gyroscope readings
        sensor_values = data.split(',')
        if len(sensor_values) == 6:
            ax, ay, az, gx, gy, gz = map(int, sensor_values)

            # Set threshold and detect gesture
            threshold = 1000
            gesture = detect_gesture(ax, ay, threshold)

            # Print detected gesture
            print("Detected Gesture:", gesture)
        
        # Add a small delay
        time.sleep(0.1)

except KeyboardInterrupt:
    # Close the serial connection on Ctrl+C
    ser.close()
