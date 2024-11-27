from django import forms
from .models import BlogPost
from django.core.exceptions import ValidationError

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'condition', 'price', 'sale_handling', 'location', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise ValidationError("Image file too large ( > 5mb )")
        return image
