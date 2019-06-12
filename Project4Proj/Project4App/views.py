from django.http import HttpResponseRedirect
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

    vidform = VideoForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        user = AccountModel.objects.get(username=request.user)
        if vidform.is_valid():
            Video.objects.create(name=request.POST["name"], videofile=request.FILES["videofile"], videoForeignKey=user)

            return redirect('index')

        context = {

            'vidform': vidform,
        }

        return render(request, 'Project4App/uploadVideo.html', context)


def videopage(request, id):
    watchvideo = get_object_or_404(Video, pk=id)

    commentform = CommentForm()

    allComments = CommentModel.objects.filter(commentForeignKey=watchvideo)

    comment = CommentForm(request.POST)

    if request.method == 'POST':

        if comment.is_valid():

            CommentModel.objects.create(text=request.POST["text"], commentForeignKey=watchvideo)
            return redirect('videoPage', id)

    context = {
        'watchvideo': watchvideo,
        'commentform': commentform,
        'comment': comment,
        'allComments': allComments
    }
    return render(request, 'Project4App/videoPage.html', context)




