from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       return reverse( 'products:product_details' ,args=[self.slug])