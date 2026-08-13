import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel matrices
Gy = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

Gx = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
], dtype=np.float32)

# Apply both masks
gx = cv2.filter2D(gray, cv2.CV_32F, Gx)
gy = cv2.filter2D(gray, cv2.CV_32F, Gy)

# Gradient magnitude
gradient = cv2.magnitude(gx, gy)

# Convert to uint8
gradient = cv2.convertScaleAbs(gradient)

# Gradient masking
sharpened = cv2.add(gray, gradient)

# Display
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened, cmap="gray")
plt.title("Gradient Masking")
plt.axis("off")

plt.show()
