from django.db import models

# Create your models here.
from datetime import datetime
from operator import mod
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    date = models.DateTimeField(default=datetime.now)
    pic = models.ImageField(null = True, blank = True, upload_to='Articlepics/')
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    pic = models.ImageField(default="Defaultprofilepic.jpg", upload_to='Profiles/')
    def __str__(self):
        return self.user.username
