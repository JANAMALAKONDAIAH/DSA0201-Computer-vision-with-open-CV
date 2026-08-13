import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Unsharp masking
sharpened = cv2.addWeighted(gray, 1.5, blur, -0.5, 0)

# Display
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened, cmap="gray")
plt.title("Unsharp Masking")
plt.axis("off")

plt.show()
