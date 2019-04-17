from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 1:1
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    nickname = models.CharField(max_length=20)
    

class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followed_by")
    