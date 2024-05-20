import serial
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set your serial port name (you may need to change it based on your system)
serial_port = "COM3"  # Change this to the appropriate serial port

# Regular expression pattern to extract RGB values from the received string
pattern = re.compile(r'B=\s*(\d+)\s+R=\s*(\d+)\s+G=\s*(\d+)')

# Initialize serial port
ser = serial.Serial(serial_port, baudrate=9600, timeout=1)

# Initialize plot
fig, ax = plt.subplots()
colors = ['blue', 'red', 'green']
bars = ax.bar(colors, [0, 0, 0], color=colors)

ax.set_ylim(0, 255)
ax.set_ylabel('RGB Values')
ax.set_title('RGB Values from Serial')

# Scaling factor to amplify the values for better visibility
scaling_factor = 2  # Adjust this factor as needed

# Function to update plot data
def update(frame):
    # Check if there is data available to read
    if ser.in_waiting > 0:
        # Read and decode the received data
        data = ser.readline().decode('utf-8').strip()
        print(data)  # Print received data for debugging
        
        # Extract RGB values using regular expression
        match = pattern.search(data)
        if match:
            rgb_values = [int(match.group(i)) for i in range(1, 4)]
            
            # Normalize the frequency values to the 0-255 range
            # Amplify the values using the scaling factor
            normalized_rgb = [min(255, int((255.0 / 1500) * val * scaling_factor)) for val in rgb_values]  # Assuming 30000 as a maximum sensor value
            
            # Update bar chart data
            for bar, value in zip(bars, normalized_rgb):
                bar.set_height(value)

            # Redraw the bar chart
            fig.canvas.draw_idle()

# Create an animation
ani = animation.FuncAnimation(fig, update, blit=False, interval=100, cache_frame_data=False)

# Show the plot
plt.show()

# Close the serial port when done
ser.close()
