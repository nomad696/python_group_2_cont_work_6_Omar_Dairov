# Generated by Django 2.1 on 2019-01-12 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Текст')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Время публикации')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.CASCADE, to='webapp.UserInfo', verbose_name='Автор'),
        ),
    ]
