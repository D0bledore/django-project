from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import the CustomUser model and forms
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Define a custom admin class for the CustomUser model
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']


# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
