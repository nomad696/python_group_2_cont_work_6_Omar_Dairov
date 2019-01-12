from django.contrib import admin
from webapp.models import UserInfo, Post


# class UserAdmin(admin.ModelAdmin):

admin.site.register(UserInfo)
admin.site.register(Post)