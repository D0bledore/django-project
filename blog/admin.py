from django.contrib import admin
from django.contrib.auth import get_user_model

# Import models to register
from .models import BlogPost

# Get the user model
User = get_user_model()

# Define a custom admin class for BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    # Override the save_model method to set the author to the current admin user
    def save_model(self, request, obj, form, change):
        # Always set the author to the current admin user
        obj.author = request.user
        super().save_model(request, obj, form, change)

# Register the BlogPost model with the custom admin class
admin.site.register(BlogPost, BlogPostAdmin)