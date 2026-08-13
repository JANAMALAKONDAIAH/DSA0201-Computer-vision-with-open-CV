import cv2

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Crop a small part
crop = img[10:60, 10:60]

# Paste the cropped part
img[70:120, 70:120] = crop

# Display
cv2.imshow("Copy and Paste", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
