import cv2
import numpy as np

img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
