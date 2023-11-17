# image_processor/urls.py
from django.urls import path
from .views import ImageProcessing

urlpatterns = [
    path('process-images/', ImageProcessing.as_view(), name='process_images'),
]