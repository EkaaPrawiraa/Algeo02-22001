# myapp/urls.py

from django.urls import path
from .views import FolderUploadView, SingleFileUploadView

urlpatterns = [
    path('upload/folder/', FolderUploadView.as_view(), name='folder_upload'),
    path('upload/single/', SingleFileUploadView.as_view(), name='single_file_upload'),
]
