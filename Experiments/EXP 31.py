import cv2

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create ORB detector
orb = cv2.ORB_create()

# Detect features
keypoints, descriptors = orb.detectAndCompute(gray, None)

# Check result
if descriptors is not None:
    print("Watch recognized in the image")
    print("Features detected:", len(keypoints))
else:
    print("Watch not recognized")

# Draw detected features
output = cv2.drawKeypoints(
    img, keypoints, None,
    color=(0, 255, 0)
)

cv2.imshow("Watch Recognition", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
