from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='projects/', blank=True)
   
   




