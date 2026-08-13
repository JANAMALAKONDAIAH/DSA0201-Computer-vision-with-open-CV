import cv2

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

if img is None:
    print("Image not found")
    exit()

# Draw rectangle
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 2)

# Extract object inside rectangle
object = img[50:250, 50:250]

# Display
cv2.imshow("Rectangle", img)
cv2.imshow("Extracted Object", object)

cv2.waitKey(0)
cv2.destroyAllWindows()
