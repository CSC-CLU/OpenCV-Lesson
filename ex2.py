import cv2
import os

# 1. Resolve path to the sample image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'sample.jpg')

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# 2. Convert to Grayscale (Edge detection works on single-channel intensity)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Apply Gaussian Blur
# Reduces background noise so false edges aren't detected
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 4. Apply Canny Edge Detection
# Threshold1 (100): Lower hysteresis bound
# Threshold2 (200): Upper hysteresis bound
edges = cv2.Canny(blurred, 100, 200)

# 5. Display the original and edge map side-by-side
cv2.imshow('Original Image', image)
cv2.imshow('Detected Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()