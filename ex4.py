import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'sample.jpg')

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# ---------------------------------------------------------
# 1. RESIZING AND RESCALING
# ---------------------------------------------------------
# Explicit dimensions (Width, Height)
resized_exact = cv2.resize(image, (300, 300))

# Proportional scaling (50% scale factor)
rescaled_half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# ---------------------------------------------------------
# 2. COLOR SPACES
# ---------------------------------------------------------
# OpenCV uses BGR by default. Common conversions:
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Great for color tracking/segmentation
rgb  = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Needed for matplotlib display

# ---------------------------------------------------------
# 3. DRAWING SHAPES AND TEXT
# ---------------------------------------------------------
# Work on a copy so the original image remains untouched
canvas = image.copy()

# Draw Line: cv2.line(img, start_point, end_point, color_bgr, thickness)
cv2.line(canvas, (0, 0), (200, 200), (0, 255, 0), 3)

# Draw Rectangle: cv2.rectangle(img, top_left, bottom_right, color_bgr, thickness)
# Note: thickness = -1 fills the shape
cv2.rectangle(canvas, (50, 50), (200, 200), (0, 0, 255), 2)

# Draw Circle: cv2.circle(img, center, radius, color_bgr, thickness)
cv2.circle(canvas, (150, 150), 40, (255, 0, 0), -1)

# Put Text: cv2.putText(img, text, origin, font, scale, color_bgr, thickness)
cv2.putText(canvas, 'OpenCV CS Club', (30, 240), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------
cv2.imshow('Rescaled 50%', rescaled_half)
cv2.imshow('HSV Color Space', hsv)
cv2.imshow('Annotated Canvas', canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()