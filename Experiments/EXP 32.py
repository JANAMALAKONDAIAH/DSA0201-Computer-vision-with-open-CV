import cv2

# Open video
video = cv2.VideoCapture(r"C:\Users\janak\OneDrive\Desktop\Open CV\EXP 3.mp4")

# Read all frames
frames = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames.append(frame)

video.release()

# Play frames in reverse
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
