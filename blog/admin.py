from django.contrib import admin
from django.contrib.auth import get_user_model

# Import models to register
from .models import BlogPost

# Register your models here.

User = get_user_model()

class BlogPostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Always set the author to the current admin user
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(BlogPost, BlogPostAdmin)