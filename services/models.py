from django.db import models

class Service(models.Model):  # Renamed from 'services'
    services_icon = models.CharField(max_length=50)
    services_title = models.CharField(max_length=50)
    services_das = models.TextField()

# Create your models here.

