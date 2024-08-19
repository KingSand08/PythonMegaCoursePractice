from . import views
from django.urls import path

# URL Patterns ex:(example.com/dogs/, where dogs is in slug), purpose is to connect the views and the models
urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'), # Will look in the slug column of the db and retrieve the slug entry for each item
    path('', views.HomeView.as_view(), name='home_view')
]
