from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class AccountModel(models.Model):
    name = models.CharField(max_length=70, default="")
    username = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=200, default="")
    password_confirm = models.CharField(max_length=200, default="")
    accountForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    videoForeignKey = models.ForeignKey(AccountModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
