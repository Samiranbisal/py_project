from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_defc = HTMLField()

# Create your models here.
