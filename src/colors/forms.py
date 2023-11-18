# forms.py
from django import forms
from .models import UploadedImage
from .models import UploadedFolder
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
class FolderUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFolder
        fields = ['folder']