import cv2

# Read the image
img = cv2.imread(r"C:\Users\janak\OneDrive\Pictures\Screenshots\Screenshot 2026-07-11 103726.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Get original size
    height, width = img.shape[:2]

    # Scale to bigger size (2 times)
    bigger = cv2.resize(img, (width * 2, height * 2))

    # Scale to smaller size (Half)
    smaller = cv2.resize(img, (width // 2, height // 2))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Save the resized images
    cv2.imwrite("bigger_image.jpg", bigger)
    cv2.imwrite("smaller_image.jpg", smaller)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
