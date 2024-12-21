from django.urls import path

# Import views
from . import views

urlpatterns = [
    path('', views.core_index, name='index'),
    path('contact/', views.core_contact, name='core_contact'),
]
