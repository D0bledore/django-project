from django import forms
from .models import BlogPost, Comment
from django.core.exceptions import ValidationError
import re


# Define a form for creating and updating BlogPost instances
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'condition',
                  'price', 'sale_handling', 'location', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the title of your post'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the content of your post'}),
            'category': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the category'}),
            'condition': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the condition (1-10)',
                       'type': 'range', 'min': '1', 'max': '10'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the price', 'max_length': 10}),
            'sale_handling': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'For example: Shipping, Pickup/Meetup'}),
            'location': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter the location'}),
            'image': forms.FileInput(
                attrs={'class': 'form-control', 'required': False}),
        }

    # Validate the title field
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise ValidationError("Title cannot exceed 100 characters.")
        return title

    # Validate the price field
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Price must be a positive number.")
        # Ensure price has up to two decimal places
        if not re.match(r'^\d+(\.\d{1,2})?$', str(price)):
            raise ValidationError("Price must have up to two decimal places.")
        # Ensure price has a maximum length of 10
        if len(str(price)) > 10:
            raise ValidationError("Price cannot exceed 10 characters.")
        return price

    # Validate the image field
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check if the uploaded image exceeds 5MB
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image file too large ( > 5MB )")
        return image


# Define a form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your comment'}),
        }

    # Validate the content field
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 500:
            raise ValidationError("Comment cannot exceed 500 characters.")
        return content
