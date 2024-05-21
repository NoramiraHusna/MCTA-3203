import cv2
import numpy as np

# Define HSV range for red color
red_lower1 = np.array([0, 120, 70])
red_upper1 = np.array([10, 255, 255])
red_lower2 = np.array([170, 120, 70])
red_upper2 = np.array([180, 255, 255])

# Define HSV range for yellow color
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

# Define HSV range for blue color
blue_lower = np.array([100, 150, 0])
blue_upper = np.array([140, 255, 255])

# Open the video capture with the default camera (index 0)
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('Failed to open the camera.')
    exit()

print("Press ESC to exit.")

while True:
    ret, frame = capture.read()
    if not ret:
        print('Failed to capture video frame.')
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for each color
    mask_red1 = cv2.inRange(hsv, red_lower1, red_upper1)
    mask_red2 = cv2.inRange(hsv, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Highlight the detected colors on separate frames
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    res_yellow = cv2.bitwise_and(frame, frame, mask=mask_yellow)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    # Display the original frame and the result frames
    cv2.imshow('Original', frame)
    cv2.imshow('Red', res_red)
    cv2.imshow('Yellow', res_yellow)
    cv2.imshow('Blue', res_blue)

    # Wait for 1 millisecond and check if ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the capture and close any OpenCV windows
capture.release()
cv2.destroyAllWindows()
print('Camera is closed')