# myapp/views.py

import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from .models import UploadedImage, Uploadeddata
from .serializers import UploadedImageSerializer, Uploadeddataset

class FolderUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        folder = request.data['folder']

        jpg_files = [f for f in os.listdir(folder) if f.lower().endswith('.jpg')]

        for jpg_file in jpg_files:
            image_path = os.path.join(folder, jpg_file)
            image_data = {'image': open(image_path, 'rb')}
            serializer = Uploadeddataset(data=image_data)
            if serializer.is_valid():
                serializer.save()
        return Response({'message': 'Images uploaded successfully'}, status=status.HTTP_201_CREATED)

class SingleFileUploadView(APIView):
    parser_classes = (MultiPartParser,FileUploadParser,)

    def post(self, request, *args, **kwargs):
        image_data = {'image': request.data['file']}
        serializer = UploadedImageSerializer(data=image_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
