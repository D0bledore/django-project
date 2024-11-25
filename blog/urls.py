from django.urls import path 

# Import views
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('posts/', views.blog_post, name='posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]