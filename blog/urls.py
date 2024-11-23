from django.urls import path 

# Import views
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('posts/', views.blog_post, name='posts'),
]