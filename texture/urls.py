# image_processor/urls.py
from django.urls import path
from .views import ImageProcessingView

urlpatterns = [
    path('process-images/', ImageProcessingView.as_view(), name='process_images'),
]