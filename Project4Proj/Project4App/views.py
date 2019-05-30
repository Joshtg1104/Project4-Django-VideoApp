from django.shortcuts import render, redirect

from .forms import VideoForm, AccountForm
from .models import Video, AccountModel


# Create your views here.


def index(request):
    allVideos = Video.objects.all()
    context = {
        'allVideos': allVideos
    }
    return render(request, 'Project4App/index.html', context)


def uploadvideo(request):

    form = VideoForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect('index')

    lastvideo = Video.objects.last()

    vids = lastvideo.videofile

    context = {
        'vids': vids,
        'form': form
    }

    return render(request, 'Project4App/uploadVideo.html', context)
