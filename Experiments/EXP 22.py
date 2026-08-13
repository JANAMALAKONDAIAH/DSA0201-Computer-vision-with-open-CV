import cv2

# Read image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\spy.png")

# Add watermark
cv2.putText(img, "WATERMARK", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 2)

# Show image
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
