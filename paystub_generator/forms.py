from django import forms
from . import models


class image_upload_form(forms.ModelForm):
    class Meta:
        model = models.image_upld
        fields = ['logo']


