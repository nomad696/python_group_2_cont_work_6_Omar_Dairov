from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from webapp.models import UserInfo, Post
from webapp.forms import PostForm, CreatePostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostListView(ListView, FormView):
    model = Post
    form_class = PostForm
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={ 'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    permission_required = 'webapp.change_post'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
