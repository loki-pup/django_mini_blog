from django.shortcuts import render

from .models import Post, Blogger, Comment

from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Post.objects.count()
    num_bloggers = Blogger.objects.count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class BloggerListView(generic.ListView):
    model = Blogger

class PostDetailView(generic.DetailView):
    model = Post

class BloggerDetailView(generic.DetailView):
    model = Blogger    