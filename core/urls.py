from django.urls import path

# Import views
from . import views

urlpatterns = [
    path('', views.core_index, name='core_index'),
]