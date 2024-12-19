from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.s3boto3 import S3Boto3Storage

class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(storage=S3Boto3Storage(), upload_to='media/profile_pics/', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(storage=S3Boto3Storage(), upload_to='media/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
