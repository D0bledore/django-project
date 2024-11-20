from django.urls import path

# Import views
from . import views

urlpatterns = [
    path('', views.core_index, name='core_index'),
    path('about/', views.core_about, name='core_about'),
    path('contact/', views.core_contact, name='core_contact'),
]