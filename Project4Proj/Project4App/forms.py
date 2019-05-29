from django import forms
from .models import Video
from django.contrib.auth.models import User


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
