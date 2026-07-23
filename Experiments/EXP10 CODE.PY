import cv2
import numpy as np

img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

src_points = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

dst_points = np.float32([
    [10, 100],
    [280, 50],
    [80, 280],
    [320, 300]
])

H, status = cv2.findHomography(src_points, dst_points)

result = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
