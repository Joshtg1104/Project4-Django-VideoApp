from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import VideoForm, AccountForm, CommentForm
from .models import Video, AccountModel, CommentModel


# Create your views here.


def base(request):
    return render(request, 'Project4App/base.html')


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

            User.objects.create_user(request.POST["username"], "", request.POST["password"])
            return redirect('index')
    context = {
        'errors': newaccountform.errors,
        'newaccountform': newaccountform
    }
    return render(request, 'Project4App/createAccount.html', context)


def uploadvideo(request):
    #This works but does not implement foreign key
    # vidform = VideoForm(request.POST or None, request.FILES or None)
    # if request.method == "POST":
    #     if vidform.is_valid():
    #         vidform.save()
    #         return redirect('index')
    # lastvideo = Video.objects.create()
    # vids = lastvideo.videofile
    # context = {
    #     'vids': vids,
    #     'vidform': vidform
    # }

    # This does not work, stops at validation because form is not valid
    vidform = VideoForm(request.POST)
    print(vidform)
    if request.user.is_authenticated:
        user = AccountModel.objects.get(username=request.user)
        print(user)
        print(request.method)
        print(vidform.is_valid)
        if vidform.is_valid():

            print("Here")
            print(vidform.is_valid())
            Video.objects.create(name=request.POST["name"], videofile=request.FILES["videofile"], videoForeignKey=user)
            vidform.save()

            return redirect('index')
        else:
            print("validation failed")

    context = {
        'vidform': vidform,
        'errors': vidform.errors
    }

    return render(request, 'Project4App/uploadVideo.html', context)


def videopage(request, id):
    watchvideo = get_object_or_404(Video, pk=id)
    videocomments = CommentModel.objects.filter(commentForeignKey=watchvideo)
    context = {
        'watchvideo': watchvideo,
        'videocomments': videocomments,
    }
    return render(request, 'Project4App/videoPage.html', context)


def commentsection(request, id):
    commentform = CommentForm(request.POST)
    if request.user.is_authenticated:
        watchvideo = get_object_or_404(Video, pk=id)
        if commentform.is_valid():
            print(request.POST)
            CommentModel.objects.create(text=request.POST["text"], commentForeignKey=watchvideo)
            return redirect('commentSection', id)
    context = {
        'comment': commentform,
        'errors': commentform.errors,
        'id': id,
    }
    return render(request, 'Project4App/videoPage.html', context)


