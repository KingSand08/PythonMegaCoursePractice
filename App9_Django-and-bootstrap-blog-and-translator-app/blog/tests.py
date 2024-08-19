from django.test import TestCase
from .models import Post

# Create your tests here.
class BlogView:
    model = Post
    template_name = 'blog.html'