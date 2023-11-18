import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .models import UploadedImage, Uploadeddata
from .serializers import UploadedImageSerializer, Uploadeddataset
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from django.core.files.storage import FileSystemStorage



class FolderUploadView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request, *args, **kwargs):
        self.clear_destination_folder(os.path.join(settings.MEDIA_ROOT, 'dataset'))
        files = request.FILES.getlist('files')

        for uploaded_file in files:
            if uploaded_file.name.lower().endswith('.jpg'):
                image_path = os.path.join(settings.MEDIA_ROOT, 'dataset', uploaded_file.name)
                with open(image_path, 'wb') as file:
                    for chunk in uploaded_file.chunks():
                        file.write(chunk)

                file_data = {'image': SimpleUploadedFile(uploaded_file.name, uploaded_file.read())}
                serializer = Uploadeddataset(data=file_data)

                if serializer.is_valid():
                    serializer.save()
                else:
                    print("Serializer errors:", serializer.errors)

        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_201_CREATED)

    def clear_destination_folder(self, folder_path):
        # Delete all files in the specified folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
                
class SingleFileUploadView(APIView):
    parser_classes = (MultiPartParser,FileUploadParser,)

    def post(self, request, *args, **kwargs):
        image_data = {'image': request.FILES['file']}
        self.clear_destination_folder(os.path.join(settings.MEDIA_ROOT, 'uploaded_images'))
        serializer = UploadedImageSerializer(data=image_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def clear_destination_folder(self, folder_path):
        # Delete all files in the specified folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

# Create your views here.
