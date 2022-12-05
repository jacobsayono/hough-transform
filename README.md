# Hough Transform

In Python, the Hough Transform can be implemented using the hough_line() and hough_circle() methods of the OpenCV library.

These methods take as input an image that has been pre-processed to detect edges, and they return the set of detected lines or circles in the form of polar coordinates.

1. `Canny edge detector` -> find edges in image

2. `Hough Transform` -> run on the edges to detect lines

3. Detected lines are drawn on the original image

# Lane Detection

The Hough Transform can be used for lane detection in images of roads.

In this case, the Hough Transform can be used to detect lines in the imagethat correspond to the lane markings on the road.

To detect lanes using the Hough Transform:

1. Read in the image and convert it to grayscale.
2. Use a `Gaussian blur` to smooth the image and reduce noise.
3. Use `Canny edge detection` to detect edges in the image.
4. Use the `Hough Transform` to detect lines in the image. You can specify a range of angles and a minimum number of points on a line to filter out false positives.
5. Iterate over the detected lines and group them into left and right lanes based on their slope and position in the image.
6. Draw the detected lanes on a copy of the original image.
