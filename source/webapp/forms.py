from django import forms
from webapp.models import UserInfo, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

    def get_create(self):
        return Post('post_detail', kwargs={'pk':self.pk})

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user', 'phone', 'avatar']