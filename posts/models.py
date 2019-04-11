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
    
    
    def __str__(self):
        return f"{self.id}: {self.content}"
    
