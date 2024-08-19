from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.
# Middleman between the html and the data

# Derived from DetailView class (as_view inherited from DetailView -> BaseDetailView -> View class)
class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'
    
class AboutView(generic.TemplateView):
    template_name='about.html'
    
class PostList(generic.ListView):
    # Gets and filters the public blog posts, which are ordered by date
    # minus date_created ensures that the ordering is newest to oldest
    queryset=Post.objects.filter(status=1).order_by('-date_created')
    template_name='index.html'