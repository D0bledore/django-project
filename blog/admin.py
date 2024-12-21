from django.contrib import admin
from django.contrib.auth import get_user_model

# Import models to register
from .models import BlogPost, Comment

# Get the user model
User = get_user_model()


# Define a custom admin class for BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    # Override the save_model method to set the author to the current admin
    def save_model(self, request, obj, form, change):
        # Always set the author to the current admin user
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Define a custom admin class for Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'author', 'content', 'active')
    actions = ['deactivate_comments']

    def deactivate_comments(self, request, queryset):
        queryset.update(active=False)
    deactivate_comments.short_description = "Deactivate selected comments"


# Register the BlogPost model with the custom admin class
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
