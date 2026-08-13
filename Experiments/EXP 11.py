import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Check image
if img is None:
    print("Image not found")
    exit()

# Direct Linear Transformation matrix
M = np.array([
    [1.5, 0, 0],
    [0, 1.5, 0]
], dtype=np.float32)

# Original size
h, w = img.shape[:2]

# Apply transformation
transformed = cv2.warpAffine(
    img,
    M,
    (int(w * 1.5), int(h * 1.5))
)

# Display
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB))
plt.title("Transformed Image")
plt.axis("off")

plt.show()
