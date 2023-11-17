# image_processor/urls.py
from django.urls import path
from .views import ImgageProcessing

urlpatterns = [
    path('process-images/', ImgageProcessing.as_view(), name='process_images'),
]