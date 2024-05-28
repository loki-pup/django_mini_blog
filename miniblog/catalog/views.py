from django.shortcuts import render

from .models import Post, Blogger, Comment

from django.views import generic

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5