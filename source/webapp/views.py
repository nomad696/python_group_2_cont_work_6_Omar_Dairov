from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from webapp.models import UserInfo, Post
from webapp.forms import PostForm, CreatePostForm
from django.shortcuts import get_object_or_404, redirect



class PostListView(ListView, FormView):
    model = Post
    template_name = 'post_list.html'
