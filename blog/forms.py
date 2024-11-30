from django import forms
from .models import BlogPost
from django.core.exceptions import ValidationError
from storages.backends.s3boto3 import S3Boto3Storage

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'condition', 'price', 'sale_handling', 'location', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            storage = S3Boto3Storage()
            if storage.size(image.name) > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image file too large ( > 5mb )")
        return image