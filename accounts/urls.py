from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.edit_profile,
         name='edit_profile'),
    path('profile/confirm_delete/<int:user_id>/',
         views.confirm_delete, name='confirm_delete'),
    path('profile/<int:user_id>/delete/',
         views.delete_profile, name='delete_account'),
    path('change_password/<int:user_id>',
         views.change_password, name='change_password'),
]
