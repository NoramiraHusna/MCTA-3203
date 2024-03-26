import serial
import time
import sys
import threading

# Function to read from serial
def serial_read(ser):
    while True:
        try:
            # Read from serial and decode bytes to string
            data = ser.readline().decode('utf-8').strip()
            print("Servo angle:", data)
        except UnicodeDecodeError:
            pass

# Main function
def main():
    try:
        # Establish serial connection
        ser = serial.Serial('COM3', 9600, timeout=1)
        print("Serial port opened successfully")

        # Start thread to continuously read from serial
        serial_thread = threading.Thread(target=serial_read, args=(ser,), daemon=True)
        serial_thread.start()

        # Main loop to check for keyboard input
        while True:
            # Check if keyboard input is available
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)
                if key.lower() == 'q':
                    break  # Quit if 'q' is pressed
                elif key.lower() == 'h':
                    ser.write(b'H')  # Send halt command to Arduino

        # Close serial connection
        ser.close()
        print("Serial port closed")

    except serial.SerialException as e:
        print("Error opening serial port:", e)

if __name__ == "__main__":
    main()
