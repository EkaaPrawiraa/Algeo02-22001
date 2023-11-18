from django.db import models

# Create your models here.
# models.py
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/query/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadedFolder(models.Model):
    folder = models.ImageField(upload_to='uploads/dataset/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProcessedImage(models.Model):
    main_image_path = models.CharField(max_length=255)
    dataset_image_path = models.CharField(max_length=255)
    percentage = models.FloatField()

    def __str__(self):
        return f"Processed Image - {self.id}"