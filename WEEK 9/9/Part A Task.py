import matplotlib.pyplot as plt
import numpy as np
import time

# Parameters
num_readings = 10
delay_time = 0.5

# Arrays to hold the readings
blue_readings = np.zeros(num_readings)
red_readings = np.zeros(num_readings)
green_readings = np.zeros(num_readings)

# Index for the current reading
read_index = 0

def create_channel(color_val):
    """Create a 10x10 block for a single color channel."""
    return np.ones((10, 10, 3)) * color_val

def create_color_block(b, r, g):
    """Create a color block for the given RGB values."""
    color = [b / 255, r / 255, g / 255]  # Normalize RGB values
    # Create a block for each channel with linear gradients
    b1 = create_channel([b / 255, 0, 0])  # Red channel
    r1 = create_channel([0, r / 255, 0])  # Green channel
    g1 = create_channel([0, 0, g / 255])  # Blue channel
    rgb_channel = [b1, r1, g1]
    # Combine the color channels horizontally
    combined_channels = np.hstack(rgb_channel)
    # Create the final RGB block for the specified color
    true_color = np.ones((10, 30, 3)) * color
    # Combine all vertically
    final_display = np.vstack([combined_channels, true_color])
    return final_display

def display_color(b, r, g):
    """Display the color with given RGB values."""
    plt.clf()  # Clear the current figure
    color_block = create_color_block(b,r, g)
    plt.imshow(color_block)
    plt.axis('off')
    
    # Add text annotations for the RGB values
    plt.text(0, 15, f'R: {int(b)}', fontsize=12, color='blue')
    plt.text(10, 15, f'G: {int(r)}', fontsize=12, color='red')
    plt.text(20, 15, f'B: {int(g)}', fontsize=12, color='green')
    
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update

def read_sensor_values():
    """Simulate reading RGB values from a sensor. Replace with actual sensor reading code."""
    return np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)

# Set up the plot
plt.ion()  # Turn on interactive mode
fig = plt.figure()

try:
    while True:
        # Read sensor values (replace with actual sensor reading)
        b, r, g = read_sensor_values()

        # Update the arrays with the new readings
        blue_readings[read_index] = b
        red_readings[read_index] = r
        green_readings[read_index] = g

        # Compute the average values
        average_red = np.mean(red_readings)
        average_green = np.mean(green_readings)
        average_blue = np.mean(blue_readings)

        # Display the color based on averaged sensor values
        display_color(average_red, average_green, average_blue)

        # Move to the next index
        read_index = (read_index + 1) % num_readings

        # Delay to make the sensor less responsive
        time.sleep(delay_time)
except KeyboardInterrupt:
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the last plot
