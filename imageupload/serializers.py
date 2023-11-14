# myapp/serializers.py
from rest_framework import serializers
from .models import UploadedImage, Uploadeddata
class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = '__all__'

class Uploadeddataset(serializers.ModelSerializer):
    class Meta:
        model = Uploadeddata
        fields = '__all__'
