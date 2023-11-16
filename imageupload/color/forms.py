# forms.py
from django import forms

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class FolderUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFolder
        fields = ['folder']
