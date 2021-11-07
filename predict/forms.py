from django import forms
from .models import Eyeimage

class EyeimageForm(forms.ModelForm):
    class Meta():
        model = Eyeimage
        fields = ("image",)
