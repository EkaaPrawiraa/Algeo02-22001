# image_processor/views.py
import os
from django.http import JsonResponse
from django.views import View
from .models import ProcessedImage
from django.conf import settings
import time
import base64
from . import functions

class ImageProcessingView(View):
    def get(self, request, *args, **kwargs):
        main_imagefolder = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')  # Adjust the main image path
        try:
            jpg_file = next(f for f in os.listdir(main_imagefolder) if f.lower().endswith('.jpg'))
        except StopIteration:
            print("Gaada foto JPG nya sayang.")
        main_image_path = os.path.join(main_imagefolder, jpg_file)
        dataset_folder = os.path.join(settings.MEDIA_ROOT, 'dataset/')

        start_time = time.time()
        processed_images = self.process_images(main_image_path, dataset_folder)
        end_time = time.time()
        total_time = end_time - start_time

        response_data = {
            'processed_images': processed_images,
            'total_time': total_time
        }

        return JsonResponse(response_data)

    def process_images(self, main_image_path, dataset_folder):
        processed_images = []
        querry_image= functions.makevector(main_image_path)
        for image_name in os.listdir(dataset_folder):
            dataset_image_path = os.path.join(dataset_folder, image_name)
            # Perform image processing and calculate percentage
            percentage = self.calculate_percentage(querry_image, dataset_image_path)
            # Save the processed image to the database
            with open(dataset_image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            if percentage>=0.60:
                percentage *= 100
                processed_images.append({
                    'image_name': image_name, 
                    'percentage': percentage,
                    'image_data': encoded_image})#harusnya encoded_image, tapi tidak dibuat karena belum ada frontend
        processed_images = sorted(processed_images, key=lambda x: x['percentage'], reverse=True)
        for image in processed_images:
            image['percentage'] = f'{image["percentage"]}%'
        return processed_images

    def calculate_percentage(self, main_image_path, dataset_image_path):
        # Read the dataset image
        percentage=functions.cosine_similarity(main_image_path, functions.makevector(dataset_image_path))
        return percentage
