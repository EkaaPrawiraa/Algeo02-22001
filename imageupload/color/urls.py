# urls.py
from django.urls import path
from .views import upload_image, upload_folder

urlpatterns = [
    path('upload_image/', upload_image, name='upload_image'),
    path('upload_folder/', upload_folder, name='upload_folder'),
    # tambahkan URL lainnya sesuai kebutuhan
]
