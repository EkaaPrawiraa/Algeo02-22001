# myapp/models.py
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
class Uploadeddata(models.Model):
    image = models.ImageField(upload_to='dataset/')
# Create your models here.
