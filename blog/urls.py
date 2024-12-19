from django.urls import path 

# Import views
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('posts/', views.blog_post, name='posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('profile/<int:user_id>/posts', views.view_posts, name='user_posts'),
]