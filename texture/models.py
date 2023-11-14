from django.db import models
import cv2
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class ImageWithPercentage(models.Model):
    image = models.ImageField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.image.name} - {self.percentage}%"

    def process_image(self):
        # Get the absolute file path of the image
        image_path = self.image.path

        # Read the image using OpenCV
        img = cv2.imread(image_path)

        # Perform image processing using OpenCV
        # For example, convert the image to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the processed image back to the storage
        processed_image_path = f"processed/{self.image.name}"
        processed_image_full_path = default_storage.path(processed_image_path)
        cv2.imwrite(processed_image_full_path, img_gray)

        # Update the ImageField to point to the processed image
        self.image = processed_image_path
        self.save()
