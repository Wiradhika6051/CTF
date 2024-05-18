import cv2

# Read the image
image = cv2.imread('images/output0001.jpg', cv2.IMREAD_GRAYSCALE)
DATA = ""
# Iterate through each pixel
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixel_value = image[i, j]
        # Process the pixel value
        if pixel_value == 0:
            # Do something for black pixels (0)
            DATA +="1"
        elif pixel_value == 255:
            # Do something for white pixels (255)
            DATA +="0"

# Display or save the processed image
cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(DATA)