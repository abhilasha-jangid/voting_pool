from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Pool(models.Model):
    title = models.CharField(max_length=200)
    question = models.TextField()
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Option(models.Model):
    name = models.CharField(max_length=30)
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Vote(models.Model):
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE)
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    
