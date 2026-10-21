import cv2

# 1. Load an image from disk
image = cv2.imread('sample.jpg')

# 2. Check the underlying matrix structure
# Returns tuple: (Height, Width, Channels)
print("Image Shape:", image.shape)

# 3. Access pixel at coordinates (y=100, x=50) -> Returns [B, G, R]
b, g, r = image[100, 50]
print(f"Pixel BGR Values: Blue={b}, Green={g}, Red={r}")

# 4. Convert BGR to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 5. Display the original image in a window
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for any key press, then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
