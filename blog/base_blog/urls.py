from django.urls import path
from .views import *


urlpatterns = [
    path('', postsList)  # blog.blog.url --> blog.base_blog.urls
]
