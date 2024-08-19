from django.db import models
from django.contrib.auth.models import User

# Defining the dev made vars here
STATUS =((0, 'Draft'), (1, 'Publish')) # Status of the choice status for a post

# Create your models here.
class Post(models.Model): # Model is a specific class that inherits from django. It is designed to contain fields with data
    title = models.CharField(max_length=200) # Title of the blog post
    contents = models.TextField() # Text of the blog post (using TextField instead as it holds more chars)
    date_created = models.DateTimeField(auto_now_add=True) # Date the blog post was made, when blog post create hits create button the time will be
        # generated and placed in date_created for the blog post instance here.
    slug = models.SlugField(max_length=200, unique=True) # Recording the part of the url after the domain
    author = models.ForeignKey(to=User, on_delete=models.CASCADE) # Is the author of the blog post, not ui input, but inserted from program.
        # (to=User) will allow usernames to be selected and this is what will populate here. (on_delete=models.CASCADE) will delete the blog
        # post if the user is also deleted
    status = models.IntegerField(choices=STATUS, default=0) # Allows content creator to choose on publishing draft as draft or as published.
    
    
    def __str__(self):
        return self.title