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

class ImgageProcessing(View):
    # def read_images_from_folder(folder_path):
    #     images = []
    #     for filename in os.listdir(folder_path):
    #         if filename.endswith((".jpg", ".jpeg", ".png")):
    #             image_path = os.path.join(folder_path, filename)
    #             image = cv2.imread(image_path)

    #             if image is not None:
    #                 images.append(image)
    #             else:
    #                 print(f"Failed to read image: {image_path}")

    #     return images

    # def process_images(self, query_image, dataset_folder):
    #     # Konversi gambar query ke ruang warna HSV dan hitung histogram
    #     hsv_query_image = colormethod.rgb_to_hsv(query_image)
    #     histogram_query_image = colormethod.calculate_histogram(hsv_query_image)

    #     # Baca gambar-gambar dari folder dataset
    #     list_images = self.read_images_from_folder(dataset_folder)

    #     # Inisialisasi daftar output
    #     output_images = []

    #     # Loop melalui setiap gambar dalam folder dan hitung kesamaan
    #     for dataset_image in list_images:
    #         hsv_data_image = colormethod.rgb_to_hsv(dataset_image)
    #         histogram_dataset_image = colormethod.calculate_histogram(hsv_data_image)

    #         similarity_image2 = 0

    #         # Loop melalui setiap blok histogram
    #         for i in range(16):
    #             similarity_image2 += colormethod.calculate_cosine_similarity(histogram_query_image[i], histogram_dataset_image[i])

    #         # Hitung rata-rata similarity
    #         similarity_image2 /= 16.0

    #         # Jika similarity lebih besar dari threshold, tambahkan ke daftar output
    #         if similarity_image2 > 0.6:
    #             output_images.append(dataset_image)

    #     return output_images
    

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
        percentage=colormethod.calculate_cosine_similarity(colormethod.calculate_histogram(colormethod.rgb_to_hsv(main_image_path)), colormethod.calculate_histogram(colormethod.rgb_to_hsv(dataset_image_path)))
        return percentage









    # def upload_image(request):
    #     if request.method == 'POST':
    #         form = ImageUploadForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             query_image = form.cleaned_data['image']

    #             # Simpan query image ke direktori 'uploads/query'
    #             query_image_path = os.path.join('uploads/query', query_image.name)
        #         with open(query_image_path, 'wb+') as destination:
        #             for chunk in query_image.chunks():
        #                 destination.write(chunk)

        #         # Proses gambar dengan dataset default
        #         dataset_folder = 'uploads/dataset'  # Ubah sesuai kebutuhan
        #         query_image = cv2.imread(query_image_path)
        #         if query_image is None:
        #             return JsonResponse({'error': 'Failed to read query image'})

        #         # Proses gambar-gambar dalam dataset
        #         output_images = process_images(query_image, dataset_folder)

        #         # Tampilkan jumlah dan nama gambar yang sesuai
        #         result = {
        #             'total_matching_images': len(output_images),
        #             'matching_images': [img.tolist() for img in output_images],
        #         }

        #         return JsonResponse(result)
        # else:
        #     form = ImageUploadForm()

        # return render(request, 'upload_image.html', {'form': form})

    # def upload_folder(self,request):
    #     if request.method == 'POST':
    #         form = self.FolderUploadForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             folder = request.FILES['folder']

    #             # Simpan folder ke direktori 'uploads/dataset'
    #             folder_path = os.path.join('uploads/dataset', folder.name)
    #             with open(folder_path, 'wb+') as destination:
    #                 for chunk in folder.chunks():
    #                     destination.write(chunk)

    #             # Tampilkan pesan sukses atau seterusnya sesuai kebutuhan
    #             return JsonResponse({'success': 'Dataset folder uploaded successfully'})
    #     else:
    #         form = FolderUploadForm()

    #     return render(request, 'upload_folder.html', {'form': form})
