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