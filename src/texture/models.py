# image_processor/models.py
from django.db import models

class ProcessedImage(models.Model):
    main_image_path = models.CharField(max_length=255)
    dataset_image_path = models.CharField(max_length=255)
    percentage = models.FloatField()

    def __str__(self):
        return f"Processed Image - {self.id}"
