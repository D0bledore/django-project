from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.s3boto3 import S3Boto3Storage


# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    # Gender choices for the user
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    # Email field set as unique and used as the username field
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Additional fields for the user
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(
        storage=S3Boto3Storage(),
        upload_to='media/profile_pics/', blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=Gender.choices, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Normalize email before saving
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


# Profile model linked to the CustomUser model
class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(
        storage=S3Boto3Storage(),
        upload_to='media/profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
