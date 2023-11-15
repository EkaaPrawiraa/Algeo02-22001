# image_processor/views.py
import os
from django.http import JsonResponse
from django.views import View
from .models import ProcessedImage
from django.conf import settings
import cv2
from PIL import Image
from . import functions

class ImageProcessingView(View):
    def get(self, request, *args, **kwargs):
        main_imagefolder = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')  # Adjust the main image path
        try:
            jpg_file = next(f for f in os.listdir(main_imagefolder) if f.lower().endswith('.jpg'))
        except StopIteration:
            print("No JPG file found in the folder.")
        main_image_path = os.path.join(main_imagefolder, jpg_file)
        dataset_folder = os.path.join(settings.MEDIA_ROOT, 'dataset/')

        processed_images = self.process_images(main_image_path, dataset_folder)
        return JsonResponse({'processed_images': processed_images})

    def process_images(self, main_image_path, dataset_folder):
        processed_images = []
        for image_name in os.listdir(dataset_folder):
            dataset_image_path = os.path.join(dataset_folder, image_name)
            # Perform image processing and calculate percentage
            percentage = self.calculate_percentage(main_image_path, dataset_image_path)
            # Save the processed image to the database
            processed_images.append({'image_name': image_name, 'percentage': percentage})
        return processed_images

    def calculate_percentage(self, main_image_path, dataset_image_path):
        # Read the dataset image
        percentage=functions.cosine_similarity(functions.makevector(main_image_path), functions.makevector(dataset_image_path))
        return percentage
