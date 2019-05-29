from django.shortcuts import render
from .models import Video
from .forms import VideoForm

# Create your views here.


def index():
    return print("Test")


def uploadvideo(request):

    lastvideo = Video.objects.last()

    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'videofile': videofile,
        'form': form
    }

    return render(request, 'index')