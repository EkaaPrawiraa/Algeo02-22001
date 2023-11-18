# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
# from .forms import ImageUploadForm, FolderUploadForm
from .cbircolor import colormethod
from PIL import Image
import cv2
import os
import time
import base64

class ImageProcessing(View):

    def get(self, request, *args, **kwargs):
        main_imagefolder = os.path.join(settings.MEDIA_ROOT, 'uploaded_images')  # Adjust the main image path
        try:
            jpg_file = next(f for f in os.listdir(main_imagefolder) if f.lower().endswith('.jpg'))
        except StopIteration:
            print("No JPG file found in the folder.")
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
        querry_image =colormethod.calculate_histogram(colormethod.rgb_to_hsv(main_image_path))
        for image_name in os.listdir(dataset_folder):
            dataset_image_path = os.path.join(dataset_folder, image_name)
            # Perform image processing and calculate percentage
            percentage = self.calculate_percentage(querry_image, dataset_image_path)
            # Save the processed image to the database
            with open(dataset_image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            if percentage>=0.60:
                percentage *= 100
                rounded_percentage = round(percentage, 2)
                rounded_percentage=f'{rounded_percentage}%'
                processed_images.append({
                    'image_name': image_name, 
                    'percentage': rounded_percentage,
                    'image_data': encoded_image})#harusnya encoded_image, tapi tidak dibuat karena belum ada frontend
        processed_images = sorted(processed_images, key=lambda x: x['percentage'], reverse=True)

        return processed_images



    def calculate_percentage(self, main_image_path, dataset_image_path):
        # Read the dataset image
    
        percentage=colormethod.calculate_cosine_similarity(main_image_path, colormethod.calculate_histogram(colormethod.rgb_to_hsv(dataset_image_path)))
        return percentage