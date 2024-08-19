from . import views
from django.urls import path

# URL Patterns ex:(example.com/dogs/, where dogs is in slug), purpose is to connect the views and the models
urlpatterns = [
    path('', views.translator_view, name='translator_view')
]
