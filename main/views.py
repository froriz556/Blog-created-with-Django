from Scripts.bottle import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Category, Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, FormView, CreateView


class MainHome(ListView):

    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostView(DetailView):

    model = Post
    template_name = 'main/posts.html'
    context_object_name = 'post'

class PostAdd(LoginRequiredMixin, CreateView):

    model = Post
    form_class = PostForm
    template_name = 'main/post_add.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


