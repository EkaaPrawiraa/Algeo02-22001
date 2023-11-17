# image_processor/urls.py
from django.urls import path
from .views import ImageProcessing

urlpatterns = [
    path('process-color-images/', ImageProcessing.as_view(), name='processed_images'),
]