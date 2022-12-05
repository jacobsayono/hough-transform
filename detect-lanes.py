import cv2
import numpy as np

# Read in the image and convert it to grayscale
image = cv2.imread('road.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use a Gaussian blur to smooth the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny edge detection to detect edges in the image
edges = cv2.Canny(blur, 50, 150)

# Use the Hough Transform to detect lines in the image
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Create arrays to store the coordinates of the left and right lanes
left_lane = []
right_lane = []

# Iterate over the detected lines and group them into left and right lanes
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    # Filter out lines that are not within a certain slope range
    slope = (y2 - y1) / (x2 - x1)
    if abs(slope) < 0.5:
        continue

    # Group the lines into left and right lanes
    if slope < 0:
        left_lane.append((x1, y1, x2, y2))
    else:
        right_lane.append((x1, y1, x2, y2))

# Use linear regression to find the best fit line for the left and right lane
left_lane = np.array(left_lane)
right_lane = np.array(right_lane)
if len(left_lane) > 0:
    left_lane = left_lane[:,0]
if len(right_lane) > 0:
    right_lane = right_lane[:,0]

# Create an image copy to draw the lanes on
lane_image = np.copy(image)