from django.db import models

# Create your models here.
class Tasks(models.Model):
    title =  models.CharField(max_length=200)
    description= models.TextField() 
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)