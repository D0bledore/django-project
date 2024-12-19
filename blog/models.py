from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100)
    condition = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_handling = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(storage=S3Boto3Storage(), upload_to='media/', blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_posts'