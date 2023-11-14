import cv2
import os

# Load the image

# Assuming your base directory is the one containing manage.py
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the path using os.path.join
relative_path = os.path.join('..','media', 'uploaded_images', '402773.jpg')
full_path = '../media/uploaded_images/402773.jpg'

# Now 'full_path' should contain the absolute path to your image

img = cv2.imread('./402773.jpg')

if img is None:
    print(f"Error: Unable to read the image from the path './402773.jpg'")
else:
    print("Image loaded successfully")

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get the RGB values of a specific pixel (e.g., pixel at row=100, column=50)
row, col = 100, 50
rgb_values = img_rgb[row, col]

print(f"RGB values at ({row}, {col}): {rgb_values}")
