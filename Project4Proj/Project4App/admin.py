from django.contrib import admin

from .models import Video, AccountModel, CommentModel

# Register your models here.


admin.site.register(AccountModel)
admin.site.register(Video)
admin.site.register(CommentModel)
