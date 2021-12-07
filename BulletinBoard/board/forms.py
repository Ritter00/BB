from django.forms import ModelForm
from django import forms
from .models import Poster, ResponseTTPoster
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PosterForm(ModelForm):

    class Meta:
        model = Poster
        fields = ['category', 'title','content',]
        widgets={
            'content': 'CKEditorUploadingWidget()',
        }