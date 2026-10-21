import cv2

# 1. Initialize video capture from default webcam (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera!")
    exit()

while True:
    # 2. Read frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame!")
        break

    # 3. Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 4. Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 5. Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)

    # 6. Display original frame and edge map
    cv2.imshow('Original Camera Feed', frame)
    cv2.imshow('Detected Edges', edges)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()