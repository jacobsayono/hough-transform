import cv2
import numpy as np

# Read in the image and convert it to grayscale
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges in the image using Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Use the Hough Transform to detect lines in the image
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Apply Gaussian blur to the image to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Use the Canny edge detector to find the edges in the image
edges = cv2.Canny(blur, 50, 150)

# Run Hough's transform on the image to detect lines
# This returns an array of (rho, theta) values for each detected line
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Iterate over the detected lines and draw them on the image
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

    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Show the image with the detected lines
cv2.imshow('Image with lines', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Canny edge detector -> find edges in image
# Hough transform -> run on the edges to detect lines
# Detected lines are drawn on the original image

# In Python, the Hough Transform can be implemented using the
# hough_line() and hough_circle() methods of the OpenCV library.
# These methods take as input an image that has been pre-processed to detect edges,
# and they return the set of detected lines or circles in the form of polar coordinates.