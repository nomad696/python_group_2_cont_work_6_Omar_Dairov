from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    # friends = models.ManyToManyField(blank=True)
    avatar = models.ImageField(verbose_name='Аватар', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    template = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True, verbose_name='Время публикации')
    author = models.ForeignKey(UserInfo,  max_length=40, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.template
