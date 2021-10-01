from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    user_banner = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    bio = models.TextField(default='Hello there! I am using Chat', max_length=225)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username