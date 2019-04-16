from django.db import models
#from django.contrib.auth.models import User 직접 접근
from django.conf import settings
# django.conf~~!!!!


# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=220)
    image = models.ImageField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.content}"
    
    
class Comment(models.Model):
    content = models.CharField(max_length=140)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
    
    def __str__(self):
        return f"{self.user}-{self.post}: {self.content}"


# class Comment_Response(models.Model):
#     content = models.CharField(max_length=140)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reponses')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
#     def __str__(self):
#         return f"{self.id}: {self.content}"

