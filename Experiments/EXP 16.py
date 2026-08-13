import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian mask with negative center coefficient
mask = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# Apply Laplacian mask
laplacian = cv2.filter2D(gray, -1, mask)

# Sharpen image
sharpened = cv2.subtract(gray, laplacian)

# Display
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpened Image")
plt.axis("off")

plt.show()
