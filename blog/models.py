from operator import mod
from pickle import FALSE
from tkinter import CASCADE
from unittest import case
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.title
  
class Reaction(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.CharField(max_length=30)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
