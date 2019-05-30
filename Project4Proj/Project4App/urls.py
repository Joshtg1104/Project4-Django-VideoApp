from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createAccount/', views.createaccount, name='createAccount'),
    path('uploadVideo/', views.uploadvideo, name='uploadVideo'),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, })
]
