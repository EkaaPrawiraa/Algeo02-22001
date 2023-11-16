# models.py
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/query/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadedFolder(models.Model):
    folder = models.ImageField(upload_to='uploads/dataset/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
