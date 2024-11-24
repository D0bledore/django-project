from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage_posts/', views.manage_posts, name='manage_posts'),
    path('publish_post/<int:post_id>/', views.publish_post, name='publish_post'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<int:user_id>/posts', views.view_posts, name='user_posts'),
]