import cv2
import pytesseract
import numpy as np

# Load the image
image = cv2.imread('xxx.png')
inverted_image = cv2.bitwise_not(image)
# Apply a threshold to create a binary image (black text will become white, background black)
_, binary_image = cv2.threshold(inverted_image, 50, 255, cv2.THRESH_BINARY_INV)
inverted_binary_image = cv2.bitwise_not(binary_image)

if len(inverted_binary_image.shape) == 3:
    inverted_binary_image = cv2.cvtColor(inverted_binary_image, cv2.COLOR_BGR2GRAY)

cv2.imshow('inverted', inverted_binary_image)

# # Find contours
# contours, _ = cv2.findContours(inverted_binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# isolated_characters = []

# # Loop over each contour and extract text if the contour is of a certain size
# for contour in contours:
#     # Get the bounding box for each contour
#     x, y, w, h = cv2.boundingRect(contour)

#     # Set a condition to filter out small or large contours that are unlikely to be isolated characters
#     # if 10 < w < 150 and 10 < h < 150:  # These dimensions may need tweaking
#         # Crop the region of interest (ROI) and perform OCR
#     roi = binary_image[y:y+h, x:x+w]
#     character = pytesseract.image_to_string(roi).strip()

#         # Only add valid single characters
#     isolated_characters.append(character)

# # Print the extracted text
# print("Extracted Text:")
# print(isolated_characters)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Extract only the capital letters
capital_letters = ''.join([char for char in extracted_text if char.isupper()])

# Print the result
print("Extracted Capital Letters:", capital_letters)

# Optional: Display the original and processed images
cv2.waitKey(0)
cv2.destroyAllWindows()