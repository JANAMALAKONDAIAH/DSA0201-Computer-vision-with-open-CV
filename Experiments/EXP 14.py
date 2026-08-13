import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel edge detection along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to displayable image
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sobel_y, cmap="gray")
plt.title("Sobel Y Edge Detection")
plt.axis("off")

plt.show()
