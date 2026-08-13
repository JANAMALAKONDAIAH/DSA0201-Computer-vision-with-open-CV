import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convolution kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply kernel
boundary = cv2.filter2D(gray, -1, kernel)

# Show result
cv2.imshow("Boundary", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
