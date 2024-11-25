from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, default='Untitled')
    content = models.TextField(default='No description provided.')
    category = models.CharField(max_length=100, default='Miscellaneous')
    condition = models.IntegerField(default=5)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sale_handling = models.CharField(max_length=100, default='pickup')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, default='', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'