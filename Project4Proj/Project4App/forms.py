from django import forms
from django.contrib.auth.models import User
from .models import Video, AccountModel


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]


class AccountForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        exclude = ["accountForeignKey"]

        def clean_password(self):
            passwordData = self.cleaned_data.get("password")
            password_confirmData = self.cleaned_data.get("password_confirm")
            print(passwordData)
            print(password_confirmData)
            if str(passwordData) != str(password_confirmData):
                raise forms.ValidationError("Password does not match")
            return passwordData

        def clean_username(self):
            usernameData = self.cleaned_data.get("username")
            print(usernameData)
            if User.objects.filter(username=usernameData).exists():
                raise forms.ValidationError("Username already in use")
            return usernameData

