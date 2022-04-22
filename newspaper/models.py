from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.
class Newspaper(models.Model):
    def __str__(self):
        return self.news_title
    
    
    news_title = models.CharField(max_length=500)
    news_decription = models.TextField(max_length=50000)
    news_video = models.CharField(max_length=1000)
    news_audio = models.CharField(max_length=1000)
    news_image = models.CharField(max_length=1000)
    news_author = models.CharField(max_length=200)
    
    
    