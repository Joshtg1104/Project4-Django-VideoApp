from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import VideoForm, AccountForm
from .models import Video, AccountModel


# Create your views here.


def index(request):
    allVideos = Video.objects.all()
    context = {
        'allVideos': allVideos
    }
    return render(request, 'Project4App/index.html', context)


def createaccount(request):
    print("OK")
    newaccountform = AccountForm(request.POST or None)
    if request.method == "POST":
        if newaccountform.is_valid():
            newaccountform.save()

            User.objects.create_user(request.POST["username"], request.POST["password"])
            return redirect('index')
    context = {
        'errors': newaccountform.errors,
        'newaccountform': newaccountform
    }
    return render(request, 'Project4App/createAccount.html', context)


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
