from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=220)
    
    
    def __str__(self):
        return f"{self.id}: {self.content}"
        

