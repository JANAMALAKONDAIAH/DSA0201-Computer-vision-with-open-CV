import cv2

# Open video
video = cv2.VideoCapture(r"C:\Users\janak\OneDrive\Desktop\Open CV\EXP 3.mp4")

# Background subtractor
bg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Detect moving objects
    mask = bg.apply(frame)

    # Find contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw boxes around detected objects
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
