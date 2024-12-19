from django import forms
from .models import BlogPost
from django.core.exceptions import ValidationError
import re

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category', 'condition', 'price', 'sale_handling', 'location', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of your post', 'required': 'required'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your post', 'required': 'required'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the category', 'required': 'required'}),
            'condition': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the condition (1-10)', 'type': 'range', 'min': '1', 'max': '10', 'required': 'required'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price', 'required': 'required'}),
            'sale_handling': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: "Pickup, as soon as possible."', 'required': 'required'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the location', 'required': 'required'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise ValidationError("Title cannot exceed 100 characters.")
        return title

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Price must be a positive number.")
        # Ensure price has up to two decimal places
        if not re.match(r'^\d+(\.\d{1,2})?$', str(price)):
            raise ValidationError("Price must have up to two decimal places.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check if the uploaded image exceeds 5MB
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Image file too large ( > 5MB )")
        return image