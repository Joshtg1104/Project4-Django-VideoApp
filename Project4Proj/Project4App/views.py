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
    #This works but does not implement foreign key
    vidform = VideoForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        user = AccountModel.objects.get(username=request.user)
        if vidform.is_valid():
            Video.objects.create(name=request.POST["name"], videofile=request.FILES["videofile"], videoForeignKey=user)
            # vidform.save()
            return redirect('index')
        # vids = newvideo.videofile
        context = {
            # 'vids': vids,
            'vidform': vidform,
        }

    # This does not work, stops at validation because form is not valid
    # vidform = VideoForm(request.POST)
    # print(vidform)
    # if request.user.is_authenticated:
    #     print(request.user)
    #     print(request.user.is_authenticated)
    #     user = AccountModel.objects.get(username=request.user)
    #     print(user)
    #     print(request.method)
    #     print(vidform.is_valid)
    #     if vidform.is_valid():
    #
    #         print("Here")
    #         print(vidform.is_valid())
    #         Video.objects.create(name=request.POST["name"], videofile=request.FILES["videofile"], videoForeignKey=user)
    #         vidform.save()
    #
    #         return redirect('index')
    #     else:
    #         print("validation failed")
    #
    # context = {
    #     'vidform': vidform,
    #     'errors': vidform.errors
    # }
    #
        return render(request, 'Project4App/uploadVideo.html', context)


def videopage(request, id):
    watchvideo = get_object_or_404(Video, pk=id)
    print(watchvideo)
    # videocomments = CommentModel.objects.filter(commentForeignKey=watchvideo)
    commentform = CommentForm()
    print(commentform)
    allComments = CommentModel.objects.filter(commentForeignKey=watchvideo)
    print(request.method)
    comment = CommentForm(request.POST)
    print(comment)
    if request.method == 'POST':
        # watchvideo = get_object_or_404(Video, pk=id)
        print(watchvideo)
        print(comment.is_valid)
        if comment.is_valid():
            print(request.POST)
            CommentModel.objects.create(text=request.POST["text"], commentForeignKey=watchvideo)
            return redirect('videoPage', id)

    context = {
        'watchvideo': watchvideo,
        'commentform': commentform,
        'comment': comment,
        'allComments': allComments
    }
    return render(request, 'Project4App/videoPage.html', context)


# def commentsection(request, id):
#
#     watchvideo = get_object_or_404(Video, pk=id)
#     print(watchvideo)
#     if request.method == 'POST':
#         commentform = CommentForm(request.POST)
#         print(commentform)
#         if commentform.is_valid():
#             comment = commentform.save(commit=False)
#             comment.watchvideo = watchvideo
#             comment.save()
#             return redirect('videoPage', id)
#     else:
#         commentform = CommentForm()
#     context = {
#         'comment': commentform,
#         'errors': commentform.errors,
#         'id': id,
#     }
#     print(commentform)
#     return render(request, 'Project4App/commentSection', context)



