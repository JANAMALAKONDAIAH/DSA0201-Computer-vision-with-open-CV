import cv2

# Read the image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\Screenshot 2026-07-11 103726.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Rotate 90° clockwise
    clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotate 90° counter clockwise
    counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

    # Save the rotated images
    cv2.imwrite("clockwise.jpg", clockwise)
    cv2.imwrite("counter_clockwise.jpg", counter_clockwise)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
